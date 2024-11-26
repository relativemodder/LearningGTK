# window.py
#
# Copyright 2024 Andrew
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# SPDX-License-Identifier: GPL-2.0-or-later

from time import strftime
from gi.repository import Gtk, Adw, GLib


@Gtk.Template(resource_path='/com/github/relative/learninggtk/window.ui')
class LearninggtkWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'LearninggtkWindow'

    timeLabel: Gtk.Label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        css_provider = Gtk.CssProvider();
        css_provider.load_from_resource("/com/github/relative/learninggtk/lovely.css")
        Gtk.StyleContext.add_provider_for_display(self.get_display(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
        self.tick()
    
    def get_time_string(self):
        time_string = strftime('%H:%M:%S')

        return time_string
    
    def tick(self):
        self.timeLabel.set_label(self.get_time_string())
        GLib.timeout_add_seconds(1, self.tick)

        return False
        
