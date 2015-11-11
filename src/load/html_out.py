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

    def append_table(self, caption, col_list, content):
        str_ = '<table>'
        # caption
        str_ += '<caption>{}</caption>'.format(caption)
        # header
        str_ += '<thead><tr>'
        str_ += ''.join(['<th>{}</th>'.format(col) for col in col_list])
        str_ += '</tr></thead>'
        # content
        str_ += '<tbody>'
        for row in content:
            str_ += '<tr>'
            str_ += ''.join(['<td>{}</td>'.format(cell) if len(cell) < 100
                             else '<td title="{}">long</td>'.format(cell)
                             for cell in row])
            str_ += '</tr>'
        str_ += '</tbody>'
        str_ += '</table>'
        self.body_str_list.append(str_)

    def append_dict_list(self, caption, dict_list):
        if not dict_list:
            return
        col_list = dict_list[0].keys()
        content = [dict_.values() for dict_ in dict_list]
        self.append_table(caption=caption, col_list=col_list, content=content)

    def __str__(self):
        str_ = self.DOCTYPE + '<html>'
        str_ += self.head()
        str_ += self.body()
        str_ += '</html>'
        return str_


def main(verbose):
    dict_list = [
        {'reg': 'F-AAAA', 'date': 'August 9th 2015'},
        {'reg': 'F-ABBB', 'date': 'November 9th 2015'},
        {'reg': 'F-CCCC', 'date': 'December 9th 2015'}]
    html = HtmlOut(verbose)
    html.append_dict_list(caption='blabla', dict_list=dict_list)
    # html.append_table(
    #     caption='test',
    #     col_list=['Date', 'Reg', 'Org', 'Dst'],
    #     content=[
    #         ['August 9th 2015', 'F-AAAA', 'LFPG', 'RJTT'],
    #         ['November 9th 2015', 'F-ABBB', 'LFPG', 'RJTT'],
    #         ['December 9th 2015', 'F-CCCC', 'LFPG', 'RJTT']
    #     ]
    # )
    print(html)

if __name__ == "__main__":
    main(verbose=True)
