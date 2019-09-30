"""
課題G: すべてのCSVにヘッダーを追加する
 Goal
すべてのcsvファイルにheaderを追加する。
headerは 氏名,メールアドレス,得点 とすること。

参考にしたURL　https://codeday.me/jp/qa/20190409/586606.html
"""
import csv


def main():
    with open('./score_data/school_a/english_score.csv', newline='', encoding='utf-8')as f:
        r = csv.reader(f)
        data = [line for line in r]

    with open('./score_data/school_a/english_score_remake.csv', 'w', newline='')as f:
        w = csv.writer(f)
        w.writerow(['氏名', 'メールアドレス', '得点'])
        for i in data:
            w.writerow(i)


if __name__ == '__main__':
    main()
