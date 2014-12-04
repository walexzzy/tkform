#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


import os
import glob
import sys
import json

import tkform


def size_of_fnames(*fnames):
  size = 0
  for fname in fnames:
    if os.path.isdir(fname):
      sub_fnames = glob.glob(os.path.join(fname, '*'))
      size += size_of_fnames(*sub_fnames)
    else:
      size += os.path.getsize(fname)
  return size


def size_str(*fnames):
  size = size_of_fnames(*fnames)
  if size < 1E6:
    return "%.3f MB" % (size/1E6)
  else:
    return "%.f MB" % (size/1E6)



class ExampleForm(tkform.Form):
  """
  Application window for Tkinter.
  """ 
  def __init__(self, width=700, height=800):
    tkform.Form.__init__(self, 'Example Form', width, height)

    # add text
    self.push_text("tkform Example", 30)
    
    # add space between rows
    self.push_spacer()
    # add dividing line
    self.push_line()

    # add a file loading list object
    self.push_text("Multiple file list loader:", 16)
    self.push_file_list_param(
        'files_and_labels',
        load_file_text='+ files')

    self.push_spacer()
    self.push_line()

    self.push_text("Multiple directory loader:", 16)
    self.push_file_list_param(
        'dirs_and_labels',
        load_dir_text='+ directory')

    self.push_spacer()
    self.push_line()

    # some text labels
    self.push_text("Labeled (file/directory) entries:", 16)
    self.push_labeled_param(
        'label1', 'enter a value for label1', 'label')
    self.push_labeled_param(
        'file2', 'enter file2', 'default_file', load_file_text='select')
    self.push_labeled_param(
        'dir3', 'enter dir3', 'default_dir', load_dir_text='select')

    self.push_spacer()
    self.push_line()

    self.push_text("Checkbox:", 16)
    self.push_checkbox_param('check4', 'check this box, or not')

    self.push_spacer()
    self.push_line()

    self.push_text("Radio Button:", 16)
    self.push_radio_param(
        'radio5',
        ['choice 0', 
         'choice 1', 
         'choice 2', 
         'choice 3'])

    self.push_spacer()
    self.push_line()

    self.push_text("Click here to run script", 16)
    self.push_submit()

    self.push_spacer()
    self.push_line()

    self.push_text("Output", 16)

    # Must register the output if you want to
    # display output during the execution of your commands
    self.push_output()


  def run(self, params):
    """
    Override the command that is run when "submit" is
    pressed.
    """

    self.clear_output()

    self.print_output('\nForm parameters:\n')

    self.print_output(json.dumps(params, indent=2))
    self.print_output('\n\n')

    fnames = [e[0] for e in params['files_and_labels']]

    self.print_output('Calculating size of files:\n')
    self.print_output('%s' % fnames)
    self.print_output('\n')
    self.print_output('Size: %s' % size_str(*fnames))
    self.print_output('\n\n')

    dirs = [e[0] for e in params['dirs_and_labels']]

    self.print_output('Calculating size of directories:\n')
    self.print_output('%s' % dirs)
    self.print_output('\n')
    self.print_output('Size: %s' % size_str(*dirs))

    self.print_output('\n\n')

    self.print_output('Close window', tkform.exit)



if __name__ == "__main__":
    form = ExampleForm(700, 900)
    form.mainloop()



