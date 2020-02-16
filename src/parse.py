import sys
import camelot
from getCollege import getCollege

def parse(input, pdf):
  print('---Parsing detected tables----')
  tables = camelot.read_pdf(pdf, pages=','.join(map(str,input)))
  tables.export('output.html', f='html', compress=True)
  #tables[0].to_csv('output.csv')
  print('---RAR File Generated---')

if __name__ == "__main__":
  path = sys.argv[1]
  code = sys.argv[2]
  print('----Searching for the pages----')
  pages = getCollege(path, code)
  print('Pages containing results of interest: {0}'.format(pages))
  parse(pages, path)