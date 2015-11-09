#!/usr/bin/python3


class HtmlOut:

    DOCTYPE = '<!DOCTYPE html>'

    CSS = '''html {font-family: sans-serif; color: #555} \
table { border-collapse: collapse; border: 1px solid #ccc} \
tr:nth-child(even) {background: #eee} \
tr:nth-child(odd) {background: #fff} \
td {padding: 0.2em 0.5em}'''

    def __init__(self, verbose=False):
        self.body_str_list = []

    def html(self):
        return self.DOCTYPE

    def head(self):
        return '<head><style>{}</style></head>'.format(self.CSS)

    def body(self):
        str_ = '<body>'
        str_ += ''.join(self.body_str_list)
        str_ += '</body>'
        return str_

    def append_table(self, col_list):
        str_ = '<table>'
        str_ += '<thead>'
        str_ += '<tr>'
        str_ += ''.join(['<th>{}</th>'.format(col) for col in col_list])
        str_ += '</tr>'
        str_ += '</thead>'
        str_ += '</table>'
        self.body_str_list.append(str_)

    def __str__(self):
        str_ = self.DOCTYPE + '<html>'
        str_ += self.head()
        str_ += self.body()
        str_ += '</html>'
        return str_



    # def append_table(self, col_list, content, caption):
    #     # Create table first
    #     caption_tag = soup.new_tag('caption', caption)
    #     th_tag = soup.new_tag('th')
    #     body = self.soup.body
    #     body.append

    # def append_dict(self, caption, dict_list):
    #     cap
    #     body = self.soup.body
    #     self.tags['table'].append(self.tags['caption'])
    #     self.tags['caption'].insert(1, caption)
    #     self.tags['table'].append(self.tags['thead'])
    #     self.tags['thead'].append(self.tags['tr'])
    #     for key in dict_list[0].keys():
    #         self.tags['tr'].append(self.tags['th'])
    #         self.tags['th'].insert(1, 'head')


def main(verbose):
    dict_list = [
        {'reg': 'F-AAAA', 'date': 'August 9th 2015'},
        {'reg': 'F-ABBB', 'date': 'November 9th 2015'},
        {'reg': 'F-CCCC', 'date': 'December 9th 2015'}]
    html = HtmlOut(verbose)
    html.append_table(col_list=['111', '222', '333'])
    print(html)

if __name__ == "__main__":
    main(verbose=True)
