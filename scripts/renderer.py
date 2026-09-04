"""
Universal Zero-Dependency Template Renderer for Family Travel Planner
Uses Jinja2 if available; otherwise uses a robust AST token-based micro-engine
supporting variables, nested for-loops, if conditions, and filters.
"""
import re

def render_template(template_content, context):
    try:
        from jinja2 import Template
        tmpl = Template(template_content)
        return tmpl.render(**context)
    except ImportError:
        return _micro_render(template_content, context)

def _tokenize(s):
    return [t for t in re.split(r'(\{%.*?%\}|\{\{.*?\}\})', s) if t]

def _micro_render(template_str, context):
    tokens = _tokenize(template_str)
    rendered, _ = _render_tokens(tokens, 0, context)
    return rendered

def _render_tokens(tokens, idx, ctx):
    out = []
    while idx < len(tokens):
        token = tokens[idx]
        if token.startswith('{%'):
            inner = token[2:-2].strip()
            if inner in ('endfor', 'endif'):
                return ''.join(out), idx
            elif inner.startswith('if '):
                cond_expr = inner[3:].strip()
                # collect if body tokens
                if_body_tokens = []
                depth = 1
                idx += 1
                while idx < len(tokens):
                    t = tokens[idx]
                    if t.startswith('{%'):
                        t_in = t[2:-2].strip()
                        if t_in.startswith('if '): depth += 1
                        elif t_in == 'endif':
                            depth -= 1
                            if depth == 0: break
                    if_body_tokens.append(t)
                    idx += 1
                
                # evaluate condition
                cond_val = _eval_expr(cond_expr, ctx)
                if cond_val:
                    rendered_body, _ = _render_tokens(if_body_tokens, 0, ctx)
                    out.append(rendered_body)
            elif inner.startswith('for '):
                m = re.match(r'for\s+([^%]+?)\s+in\s+([^%]+)', inner)
                if not m:
                    idx += 1
                    continue
                vars_part = [v.strip() for v in m.group(1).split(',')]
                iter_expr = m.group(2).strip()
                
                # collect loop body tokens
                loop_body_tokens = []
                depth = 1
                idx += 1
                while idx < len(tokens):
                    t = tokens[idx]
                    if t.startswith('{%'):
                        t_in = t[2:-2].strip()
                        if t_in.startswith('for '): depth += 1
                        elif t_in == 'endfor':
                            depth -= 1
                            if depth == 0: break
                    loop_body_tokens.append(t)
                    idx += 1
                
                # evaluate iterable
                items = _eval_expr(iter_expr, ctx) or []
                for item in items:
                    sub_ctx = dict(ctx)
                    if len(vars_part) == 1:
                        sub_ctx[vars_part[0]] = item
                    else:
                        for i, v_name in enumerate(vars_part):
                            sub_ctx[v_name] = item[i] if i < len(item) else ''
                    rendered_body, _ = _render_tokens(loop_body_tokens, 0, sub_ctx)
                    out.append(rendered_body)
        elif token.startswith('{{'):
            expr = token[2:-2].strip()
            val = _eval_expr(expr, ctx)
            out.append(str(val if val is not None else ''))
        else:
            out.append(token)
        idx += 1
    return ''.join(out), idx

def _eval_expr(expr, ctx):
    if '|' in expr:
        parts = expr.split('|')
        val = _eval_single(parts[0].strip(), ctx)
        for f in parts[1:]:
            f = f.strip()
            if f.startswith('replace('):
                m_rep = re.search(r'replace\(\s*([\'\"])(.*?)\1\s*,\s*([\'\"])(.*?)\3\s*\)', f)
                if m_rep and isinstance(val, str):
                    old_s = m_rep.group(2).encode().decode('unicode-escape')
                    new_s = m_rep.group(4).encode().decode('unicode-escape')
                    val = val.replace(old_s, new_s)
        return val
    return _eval_single(expr, ctx)

def _eval_single(expr, ctx):
    expr = expr.strip()
    if '.split(' in expr:
        m = re.match(r'([^.]+)\.split\(\s*([\'\"])(.*?)\2\s*\)\[(\d+)\]', expr)
        if m:
            base = str(_eval_single(m.group(1), ctx))
            sep = m.group(3)
            idx = int(m.group(4))
            p = base.split(sep)
            return p[idx] if idx < len(p) else ''
    if '[:' in expr:
        m = re.match(r'([^\[]+)\[:(\d+)\]', expr)
        if m:
            base = str(_eval_single(m.group(1), ctx))
            return base[:int(m.group(2))]
    if '[' in expr and expr.endswith(']'):
        m = re.match(r'([^\[]+)\[(\d+)\]', expr)
        if m:
            base = _eval_single(m.group(1), ctx)
            idx = int(m.group(2))
            if isinstance(base, (list, tuple)) and idx < len(base):
                return base[idx]
            return ''
    parts = expr.split('.')
    curr = ctx
    for p in parts:
        if isinstance(curr, dict) and p in curr: curr = curr[p]
        elif hasattr(curr, p): curr = getattr(curr, p)
        else: return ''
    return curr
