import re

from lxml import etree

def parse_activities(activity_file):
    parser = etree.XMLParser(ns_clean=True)
    # import pudb; pudb.set_trace()
    tree = XMLTree(etree.parse(activity_file, parser)).objectify()
    return tree

    # for activities in tree.Activities:
        # for activity in activities.Activity:
            # for lap in activity.Lap:
                # for track in lap.Track:
                    # for point in track.Trackpoint:
                        # print point.DistanceMeters.text
                        # print point.Time.text
                        # print '-'*10

def clean_tag(tag):
    return re.sub('{.*?}', '', tag)

class XMLTree(object):
    def __init__(self, tree=None, parent=None, name='root'):
        self.tree = tree
        self.parent = parent
        self.name = name
        self.children = set()
        self.objectifying = False

        # self.initializing = True
        # self.__base_attrs = {'__members__', '__methods__'}
        # self.__base_attrs |= set(dir(self))
        # self.initializing = False

    def __repr__(self):
        return 'XMLTree Obj: Root --> {}'.format(self.name)

    def __str__(self):
        return 'XMLTree Obj: Root --> {}'.format(self.name)

    def __getattr__(self, attr):
        # if self.initializing:
            # raise AttributeError('No such attribute: {}'.format(attr))
        if self.objectifying:
            setattr(self, attr, [])
            return getattr(self, attr)
        else:
            # print "Traversing for {}...".format(attr)
            # Traverse down the tree, attempting to find the tag.
            roots = []
            leaves = []
            for child in self.children:
                child_tree = getattr(self, child)
                for tree in child_tree:
                    try:
                        root = getattr(tree, attr)
                    except AttributeError:
                        break
                    else:
                        if isinstance(root, list):
                            roots.extend(root)
                        else:
                            leaves.append(root)


            if not roots and not leaves:
                raise AttributeError('No such attribute: {}'.format(attr))
            else:
                return roots or leaves

                # roots.append(self.child.

            # if tree_root:
                # return tree_root
            # else:

            # return roots

        # return getattr(self, attr)

    # def find(self):


    # @property
    # def children(self):
        # return set(dir(self)) - self.__base_attrs

    # def first(self, attr):

    def objectify(self, element=None, parent=None):
        if parent is None:
            tree_root = self
            element = self.tree.getroot()
        else:
            tree_root = parent

        tree_root.objectifying = True
        for tag in element:
            cleaned_tag = clean_tag(tag.tag)
            if not len(tag):
                tree_root.children.add(cleaned_tag)
                setattr(tree_root, cleaned_tag, tag)
            else:
                tree_root.children.add(cleaned_tag)
                sub_tree_root = XMLTree(parent=tree_root, name=cleaned_tag)
                getattr(tree_root, cleaned_tag).append(self.objectify(tag, sub_tree_root))

        tree_root.objectifying = False
        return tree_root

    @property
    def leaf_nodes(self):
        leaves = []
        # for tree in self


    # def objectifying(self, bool_):
        # self.objectified = not bool_

