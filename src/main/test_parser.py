def parse_text(s: str):
    s_arr = [tuple(ss.strip().splitlines()) for ss in s.split('\n\n') if len(ss.strip()) > 0]
    return s_arr