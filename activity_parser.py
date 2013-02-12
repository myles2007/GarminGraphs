import re

from lxml import etree

def parse_activities(activity_file):
    parser = etree.XMLParser(ns_clean=True)
    tree = XMLTree(etree.parse(activity_file, parser)).objectify()

    for activities in tree.Activities:
        for activity in activities.Activity:
            for lap in activity.Lap:
                for track in lap.Track:
                    for point in track.Trackpoint:
                        print point.DistanceMeters.text
                        print point.Time.text
                        print '-'*10

def clean_tag(tag):
    return re.sub('{.*?}', '', tag)

class XMLTree(object):
    def __init__(self, tree=None, parent=None, name='root'):
        self.tree = tree
        self.parent = parent
        self.initializing = False
        self.name = name

    def __repr__(self):
        return 'XMLTree Obj: Root --> {}'.format(self.name)

    def __str__(self):
        return 'XMLTree Obj: Root --> {}'.format(self.name)

    def objectify(self, element=None, parent=None):
        if parent is None:
            tree_root = self
            element = self.tree.getroot()
        else:
            tree_root = parent

        tree_root.initialized(False)
        for tag in element:
            cleaned_tag = clean_tag(tag.tag)
            if not len(tag):
                setattr(tree_root, cleaned_tag, tag)
            else:
                sub_tree_root = XMLTree(parent=tree_root, name=cleaned_tag)
                getattr(tree_root, cleaned_tag).append(self.objectify(tag, sub_tree_root))

        tree_root.initialized(True)
        return tree_root

    def __getattr__(self, attr):
        if self.initializing:
            setattr(self, attr, [])
        else:
            raise AttributeError('No such attribute: {}'.format(attr))

        return getattr(self, attr)

    def initialized(self, bool_):
        self.initializing = not bool_

