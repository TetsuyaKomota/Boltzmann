# coding = utf-8

import unittest
from models.StrTape import StrTape

"""
Todo リスト

・str から生成するコンストラクタ
    ・大文字
    ・小文字

----------------------------------------
完了
・7次元バイナリの出力 getNext
    ・tapeList から順繰りに
    ・出力したら後ろに戻る
    ・出切ったらアナウンス
・桁数指定して表示 show
・周期の長さを取得
・str から生成するコンストラクタ
    ・S
    ・C
    ・I
    ・E
    ・N
    ・C
    ・E
 
"""

class TDD(unittest.TestCase):

    def test_getNext(self):
        tape = StrTape()
        tape.pushCode([0, 0, 0, 0, 0, 0, 0])
        code = tape.getNext()
        self.assertEquals(\
                code, \
                [True, [0, 0, 0, 0, 0, 0, 0]])

    def test_getNext_repeat(self):
        tape = StrTape()
        tape.appendCode([0, 0, 0])
        tape.appendCode([0, 0, 1])
        tape.appendCode([0, 1, 0])

        codeList = []

        codeList.append(tape.getNext())
        codeList.append(tape.getNext())
        codeList.append(tape.getNext())
        codeList.append(tape.getNext())

        self.assertEquals(\
                codeList, \
                [\
                    [False, [0, 0, 0]],\
                    [False, [0, 0, 1]],\
                    [True,  [0, 1, 0]],\
                    [False, [0, 0, 0]]\
                ])

    def test_getLength(self):
        tape = StrTape()
        tape.appendCode([0, 0, 0])
        tape.appendCode([0, 0, 1])
        tape.appendCode([0, 1, 0])
        tape.appendCode([0, 1, 1])
        tape.appendCode([1, 0, 0])
        
        length = tape.getLength()
        
        self.assertEquals(length, 5)

 
    def test_show(self):
        tape = StrTape()
        tape.appendCode([0, 0, 0])
        tape.appendCode([0, 0, 1])
        tape.appendCode([0, 1, 0])
        tape.appendCode([0, 1, 1])
        tape.appendCode([1, 0, 0])
        
        show = tape.show(10)

        self.assertEquals(\
            show, \
            [\
                "0000100001", \
                "0011000110", \
                "0101001010", \
            ])

    def test_inputAlph_S(self):
        tape = StrTape()
        tape.inputStr("S")

        length = tape.getLength()
        show   = tape.show(length*2)

        self.assertEquals(
            show, \
            [\
                "0011100111", \
                "0100001000", \
                "0100001000", \
                "0011000110", \
                "0000100001", \
                "0000100001", \
                "0111001110"\
            ]        
        )

    def test_inputStr_SCIENCE(self):
        tape = StrTape()
        tape.inputStr("SCIENCE")
        
        length = tape.getLength()
        show   = tape.show(length)

        self.assertEquals(
            show, \
            [\
                "00111001100111011110100010011001111", \
                "01000010010010010000100010100101000", \
                "01000010000010010000110010100001000", \
                "00110010000010011100101010100001110", \
                "00001010000010010000100110100001000", \
                "00001010010010010000100010100101000", \
                "01110001100111011110100010011001111"  \
            ]        
        )



if __name__ == "__main__":
    unittest.main()
