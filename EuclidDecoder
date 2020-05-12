#!/usr/bin/python
# -*- coding: utf-8 -*
import sys

__author__ = "gisly"
import xml.etree.ElementTree as ET


def decode_file(filename):
    log_filename = filename + '_processing.log'
    with open(log_filename, 'w', encoding='utf-8') as log_out:
        #парсим файл как XML
        tree = ET.parse(filename)
        #получаем абзацы
        paragraphs = tree.findall('.//body/para')
        for paragraph in paragraphs:
            #получаем предложения
            sentences = paragraph.findall('./se')
            for sentence in sentences:
                if sentence.text:
                    try:
                        #читаем текст как windows-1251
                        element_text_decoded = bytes(sentence.text, 'cp1251').decode('utf-8')
                        #записываем в XML
                        sentence.text = element_text_decoded
                    except Exception as e:
                        log_out.write("error for paragraph %s (sentence %s): %s : %s\r\n" %
                              (paragraph.attrib['id'], sentence.attrib['variant_id'], sentence.text, e))
                      
                        letter_to_replace = 'Р'
                        text_cut = sentence.text.replace(letter_to_replace, '$!$')
                        letter_to_replace2 = 'вЂ'
                        text_cut = text_cut.replace(letter_to_replace2, '$_$')

                        element_text_decoded = bytes(text_cut, 'cp1251').decode('utf-8').\
                            replace('$!$', 'И'). \
                            replace('$_$', ' ')
                    sentence.text = element_text_decoded
                    print(paragraph.attrib['id'], sentence.attrib['variant_id'])
        #пишем результат
        tree.write(filename + '_out.xml', encoding='utf-8')


def main():
    if len(sys.argv) < 2:
        print("usage: decode_bad_xml.py <filename>")
        return
    filename = sys.argv[1]
    print("decoding %s" % filename)
    decode_file(filename)


if __name__ == "__main__":
    main()
