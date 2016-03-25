#!/usr/bin/python

class Book:
  def __init__(self):
    self.title = None
    self.author = None
    self.colors = {'header': '{c',
                   'subheader': '{D',
                   'body': '{x',
                   'footer': '{c'}
    self.sections = []

  def set_title(self,title):
    self.title = title

  def set_author(self,author):
    self.author = author

  def set_colors(self,colors):
    for key,value in colors.iteritems():
      self.colors[key] = value

  def add_section(self,section):
    self.sections.append(section)

class Section:
  def __init__(self):
    self.name = None
    self.pages = []

  def set_name(self,name):
    self.name = name

  def add_page(self,page):
    self.pages.append(page)

class Page:
  def __init__(self):
    self.maxrows = 0
    self.lines = []

  def set_maxrows(self,maxrows):
    self.maxrows = int(maxrows)

  def add_line(self,line):
    if len(self.lines) <= self.maxrows:
      self.lines.append(line)
      return True
    else:
      return False
