import xmltree


    for lap in tree.Lap:
        import pudb; pudb.set_trace()

def parse_activity(activity_file):
    tree = xmltree.XMLTree(xml=activity_file).objectify()
    return tree

    # for speed_point in tree.HeartRateBpm:
        # print '*' * int(speed_point.Value.text)

    # for activities in tree.Activities:
        # for activity in activities.Activity:
            # for lap in activity.Lap:
                # for track in lap.Track:
                    # for point in track.Trackpoint:
                        # print point.DistanceMeters.text
                        # print point.Time.text
                        # print '-'*10
