import tkinter as t
from tkinter import messagebox as msg
import ArithmeticAlgorithm as ar
import HuffmanAlgorithm as ha
import LZWAlgorithm as lzw

import Utilities as u

root = t.Tk()
root.title("Endoce & Decode Message")
root.minsize(height=450, width=850)

# title
lblTitle = t.Label(text="Endoce & Decode Message", font=u.kTitleFONT)
lblTitle.pack()
lblTitle.place(x=250, y=15)

lblMessage = t.Label(text="Orignial Message", font=u.kLblFONT)
lblMessage.pack()
lblMessage.place(x=15, y=65)

txtOriginalMessage = t.Entry(width=50, font=u.kLblFONT)
txtOriginalMessage.pack()
txtOriginalMessage.place(x=175, y=68)

varAlgorithmType = t.IntVar()
rdbArthmeticAlgorithm = t.Radiobutton(
    root, text="Arthmetic Algorithm", variable=varAlgorithmType, value=1, font=u.kLblFONT)
rdbArthmeticAlgorithm.pack()
rdbArthmeticAlgorithm.place(x=170, y=120)

rdbHuffmanAlgorithm = t.Radiobutton(
    root, text="Huffman Algorithm", variable=varAlgorithmType, value=2, font=u.kLblFONT)
rdbHuffmanAlgorithm.pack()
rdbHuffmanAlgorithm.place(x=370, y=120)

rdbLZWAlgorithm = t.Radiobutton(
    root, text="LZW Algorithm", variable=varAlgorithmType, value=3, font=u.kLblFONT)
rdbLZWAlgorithm.pack()
rdbLZWAlgorithm.place(x=560, y=120)

lblEncodeMessage = t.Label(text="Encode Message", font=u.kLblFONT)
lblEncodeMessage.pack()
lblEncodeMessage.place(x=15, y=270)

txtEncodeMessage = t.Entry(width=50, font=u.kLblFONT)
txtEncodeMessage.pack()
txtEncodeMessage.place(x=175, y=270)

lblDecodeMessage = t.Label(text="Decode Message", font=u.kLblFONT)
lblDecodeMessage.pack()
lblDecodeMessage.place(x=15, y=320)

txtDecodeMessage = t.Entry(width=50, font=u.kLblFONT)
txtDecodeMessage.pack()
txtDecodeMessage.place(x=175, y=320)


def EncodeMessage():
    txtEncodeMessage.delete(0, t.END)
    txtDecodeMessage.delete(0, t.END)

    originalMessageValue = txtOriginalMessage.get()
    if len(originalMessageValue.strip()) == 0:
        msg.showerror("Error", "Message must not be empty!")
        return

    algorithmTypeValue = varAlgorithmType.get()
    if algorithmTypeValue not in [1, 2, 3]:
        msg.showerror("Error", "Select Algorithm!")
        return

    if algorithmTypeValue == 1:
        dict_of_symbols = ar.calculate_symbols(originalMessageValue)
        prob_tbl = ar.get_probability_table(dict_of_symbols)
        encode_value = ar.encode(originalMessageValue, prob_tbl)
        txtEncodeMessage.insert(0, encode_value)
    elif algorithmTypeValue == 2:
        encoding, the_tree = ha.HuffmanEncoding(originalMessageValue)
        # print(encoding, the_tree)
        txtEncodeMessage.insert(0, encoding)
    elif algorithmTypeValue == 3:
        encoding_msg = lzw.compress(originalMessageValue)
        print(encoding_msg)
        txtEncodeMessage.insert(0, encoding_msg)


def DecodeMessage():
    txtEncodeMessage.delete(0, t.END)
    txtDecodeMessage.delete(0, t.END)

    originalMessageValue = txtOriginalMessage.get()
    if len(originalMessageValue.strip()) == 0:
        msg.showerror("Error", "Message must not be empty!")
        return

    algorithmTypeValue = varAlgorithmType.get()
    if algorithmTypeValue not in [1, 2, 3]:
        msg.showerror("Error", "Select Algorithm!")
        return

    if algorithmTypeValue == 1:
        encoded_msg = txtEncodeMessage.get()
        dict_of_symbols = ar.calculate_symbols(originalMessageValue)
        prob_tbl = ar.get_probability_table(dict_of_symbols)
        decode_msg = ar.decode(encoded_msg, len(encoded_msg), prob_tbl)
        txtDecodeMessage.insert(0, decode_msg)

    elif algorithmTypeValue == 2:
        encoding, the_tree = ha.HuffmanEncoding(originalMessageValue)
        print(encoding, the_tree)
        txtEncodeMessage.insert(0, encoding)
        decoding = ha.HuffmanDecoding(encoding, the_tree)
        txtDecodeMessage.insert(0, decoding)

    elif algorithmTypeValue == 3:
        encoding_msg = txtEncodeMessage.get()
        decoding_msg = lzw.decompress(encoding_msg)
        txtDecodeMessage.insert(0, encoding_msg)


btnEncode = t.Button(root, text="ENCODE", font=(
    "Arial", 18, "bold"), command=EncodeMessage)
btnEncode.pack()
btnEncode.place(x=250, y=200)

btnDecode = t.Button(root, text="DECODE", font=(
    "Arial", 18, "bold"), command=DecodeMessage)
btnDecode.pack()
btnDecode.place(x=450, y=200)


root.mainloop()
