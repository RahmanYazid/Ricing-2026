#!/usr/bin/env python3
import math
import re

# ─── ANSI Colors ────────────────────────────────────────────────────────────
RESET   = "\033[0m"
BOLD    = "\033[1m"
DIM     = "\033[2m"
PURPLE  = "\033[1;35m"
BLUE    = "\033[1;34m"
GREEN   = "\033[1;32m"
RED     = "\033[1;31m"
CYAN    = "\033[1;36m"
WHITE   = "\033[1;37m"
GRAY    = "\033[0;37m"
YELLOW  = "\033[1;33m"

# ─── Display Width ───────────────────────────────────────────────────────────
WIDTH = 35

def format_number(value) -> str:
    """
    Format angka seperti Windows Calculator:
    - Integer → 1,000,000
    - Float   → 1,000,000.00  (strip trailing zeros tapi min 2 desimal jika ada titik)
    - Jika desimal terlalu panjang, batasi ke 10 digit signifikan
    """
    if isinstance(value, complex):
        return str(value)

    if isinstance(value, float):
        # Cek apakah sebenarnya bilangan bulat
        if value.is_integer() and abs(value) < 1e15:
            return f"{int(value):,}"
        # Format float: sampai 10 desimal, strip trailing zeros, min 2 desimal
        formatted = f"{value:,.10f}".rstrip('0')
        # Pastikan minimal 2 angka di belakang koma
        dot_idx = formatted.find('.')
        if dot_idx != -1:
            decimals = len(formatted) - dot_idx - 1
            if decimals < 2:
                formatted = formatted + '0' * (2 - decimals)
        return formatted
    elif isinstance(value, int):
        return f"{value:,}"
    else:
        return str(value)

def format_expression(expr: str) -> str:
    """Rapikan tampilan ekspresi: ganti ** → ^, * → ×, / → ÷"""
    expr = re.sub(r'\*\*', '^', expr)
    expr = re.sub(r'\*', '×', expr)
    expr = re.sub(r'/', '÷', expr)
    return expr

def draw_line(char="─", color=PURPLE) -> str:
    return f"{color}{char * WIDTH}{RESET}"

def draw_box_top(color=PURPLE) -> str:
    return f"{color}╭{'─' * (WIDTH - 2)}╮{RESET}"

def draw_box_bottom(color=PURPLE) -> str:
    return f"{color}╰{'─' * (WIDTH - 2)}╯{RESET}"

def draw_box_row(text: str, color=PURPLE, text_color=WHITE, align="right") -> str:
    inner = WIDTH - 4  # padding kiri-kanan 1
    if align == "right":
        content = text[:inner].rjust(inner)
    elif align == "left":
        content = text[:inner].ljust(inner)
    else:
        content = text[:inner].center(inner)
    return f"{color}│ {text_color}{content}{color} │{RESET}"

def print_header():
    print()
    print(draw_box_top(PURPLE))
    print(draw_box_row("HYPR-CALC", PURPLE, CYAN, "center"))
    print(draw_box_row("Standard Calculator", PURPLE, GRAY, "center"))
    print(draw_box_bottom(PURPLE))

def print_help():
    print(f"\n{GRAY}{'─' * WIDTH}")
    print(f"  {YELLOW}Fungsi yang tersedia:{RESET}")
    helps = [
        ("sin/cos/tan(x)",  "trigonometri"),
        ("sqrt(x)",         "akar kuadrat"),
        ("log(x)",          "log basis 10"),
        ("log2(x)",         "log basis 2"),
        ("ln(x) / log(x,e)","log natural"),
        ("x**y  atau x^y",  "pangkat"),
        ("pi / e",          "konstanta"),
        ("abs(x)",          "nilai mutlak"),
        ("floor/ceil(x)",   "pembulatan"),
        ("factorial(x)",    "faktorial"),
    ]
    for func, desc in helps:
        print(f"  {CYAN}{func:<20}{GRAY}{desc}{RESET}")
    print(f"  {CYAN}{'cls / clear':<20}{GRAY}bersihkan layar{RESET}")
    print(f"  {CYAN}{'history':<20}{GRAY}tampilkan riwayat{RESET}")
    print(f"  {CYAN}{'exit / q':<20}{GRAY}keluar{RESET}")
    print(f"{GRAY}{'─' * WIDTH}{RESET}\n")

def print_history(history: list):
    if not history:
        print(f"\n{GRAY}  (belum ada riwayat){RESET}\n")
        return
    print(f"\n{GRAY}{'─' * WIDTH}")
    print(f"  {YELLOW}Riwayat Perhitungan:{RESET}")
    for i, (expr, result) in enumerate(history[-10:], 1):
        expr_disp  = format_expression(expr)
        result_disp = format_number(result)
        print(f"  {GRAY}{i:>2}. {CYAN}{expr_disp} {GRAY}= {GREEN}{result_disp}{RESET}")
    print(f"{GRAY}{'─' * WIDTH}{RESET}\n")

def preprocess(expr: str) -> str:
    """Ganti notasi ^ → ** dan tanda × ÷ jika user pakai."""
    expr = expr.replace('^', '**')
    expr = expr.replace('×', '*')
    expr = expr.replace('÷', '/')
    # Tambah 'ln' sebagai alias log natural
    expr = re.sub(r'\bln\s*\(', 'log(', expr)
    return expr

def print_result_display(expr: str, result):
    """Tampilkan layar kalkulator: ekspresi di atas, hasil besar di bawah."""
    expr_disp   = format_expression(expr)
    result_disp = format_number(result)

    print()
    print(f"{PURPLE}╭{'─' * (WIDTH - 2)}╮{RESET}")
    # Baris ekspresi (kecil, di atas, rata kanan)
    max_expr = WIDTH - 6
    if len(expr_disp) > max_expr:
        expr_disp = "…" + expr_disp[-(max_expr - 1):]
    print(draw_box_row(expr_disp + "  =", PURPLE, GRAY, "right"))
    # Baris hasil (besar, tebal, rata kanan)
    max_res = WIDTH - 4
    if len(result_disp) > max_res:
        result_disp = result_disp[:max_res - 1] + "…"
    print(draw_box_row(result_disp, PURPLE, f"{BOLD}{GREEN}", "right"))
    print(f"{PURPLE}╰{'─' * (WIDTH - 2)}╯{RESET}")
    print()

def print_error(msg: str):
    print(f"\n{RED}  ✗ Error: {msg}{RESET}\n")

def main():
    print_header()
    print(f"\n{GRAY}  Ketik {CYAN}help{GRAY} untuk daftar fungsi.")
    print(f"  Ketik {CYAN}exit{GRAY} untuk keluar.{RESET}\n")

    history: list = []     # list of (expr_str, result)
    last_result = None     # ANS: hasil terakhir

    # Siapkan namespace math: semua fungsi + konstanta
    math_ns = vars(math).copy()
    math_ns["ans"] = 0      # alias hasil terakhir

    while True:
        try:
            prompt = f"{PURPLE}›{RESET} "
            user_input = input(prompt).strip().strip('\r')

            if not user_input:
                continue

            low = user_input.lower()

            # ── Perintah khusus ─────────────────────────────────────────
            if low in ('exit', 'quit', 'q'):
                print(f"\n{PURPLE}  Goodbye!{RESET}\n")
                break

            if low in ('help', '?'):
                print_help()
                continue

            if low in ('history', 'hist'):
                print_history(history)
                continue

            if low in ('cls', 'clear'):
                print("\033[2J\033[H", end="")
                print_header()
                continue

            if low in ('cls history', 'clear history', 'ch'):
                history.clear()
                print(f"\n{GRAY}  Riwayat dihapus.{RESET}\n")
                continue

            # ── Evaluasi ekspresi ────────────────────────────────────────
            expr_clean = preprocess(user_input)

            # Update ANS
            math_ns["ans"] = last_result if last_result is not None else 0

            result = eval(expr_clean, {"__builtins__": None}, math_ns)

            # Simpan dan tampilkan
            history.append((user_input, result))
            last_result = result
            math_ns["ans"] = result

            print_result_display(user_input, result)

        except KeyboardInterrupt:
            print(f"\n{PURPLE}  Goodbye!{RESET}\n")
            break
        except ZeroDivisionError:
            print_error("Tidak bisa dibagi nol")
        except ValueError as e:
            print_error(f"Nilai tidak valid — {e}")
        except SyntaxError:
            print_error("Ekspresi tidak valid")
        except Exception as e:
            print_error(str(e))

if __name__ == "__main__":
    main()
