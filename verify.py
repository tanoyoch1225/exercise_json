from pprint import pprint
from solution import solution

# VERIFICATION SCRIPT - DO NOT MODIFY

if __name__ == "__main__":
    CORRECT_RESULT = ["オーロット", "ダーテング", "トロピウス", "パンプジン", "メブキジカ", "モジャンボ", "ルンパッパ"]
    your_solution = solution()

    if your_solution == CORRECT_RESULT:
        print("ヽ(*＾ω＾*)ﾉ　ヽ(*＾ω＾*)ﾉ　ヽ(*＾ω＾*)ﾉ")
        print("よくできました！")
        print("ヽ(*＾ω＾*)ﾉ　ヽ(*＾ω＾*)ﾉ　ヽ(*＾ω＾*)ﾉ")
    else:
        print("答えは合っていません。＞＜")
        print("あなたの答え：")
        pprint(your_solution)
        print("正しい答え：")
        pprint(CORRECT_RESULT)
