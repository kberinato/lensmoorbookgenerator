#!/usr/bin/python
print "Content-type: text/plain;charset=utf-8"
print
import cgi
import xml.etree.ElementTree as ET
import bookclasses

MAXROWS = 21
MAXCOLS = 76

def get_colored_length(text):
  codes = text.count("{.")
  truelength = len(text) - (codes * 2)
  return truelength

def wrap_text(section):
  section_wrapped = []
  for paragraph in section.text.split('\n'):
   if len(paragraph) > 0:
     para_wrapped = ['']
     words = paragraph.text.split(' ')
     for word in words:
       truelength = get_colored_length(word)
       if (truelength + len(para_wrapped[:1])) >= MAXCOLS:
         section_wrapped.append(para_wrapped)
         para_wrapped = ['']
       para_wrapped[:1].append(word)
  return section_wrapped
       
def main():
  form = cgi.FieldStorage()
  
  if not form:
    raw  = ET.parse("book.xml")
  else:
    text = form["book"].value
    raw = ET.fromstring(text)

  book = bookclasses.Book()
  color_dict = raw.find("colors").attrib
  if color_dict:
    book.set_colors(color_dict) 
  rawsections = raw.findall('section')
  for s in rawsections:
    section = bookclasses.Section()
    section_name = s[0].attrib('name')
    section_text = s[0].text
    section.set_name(section_name)
    
    book.add_section(wrap_text(

main()
