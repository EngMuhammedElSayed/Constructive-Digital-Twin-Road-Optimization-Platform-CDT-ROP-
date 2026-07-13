from standards.manager import StandardsManager

standards = StandardsManager()

road_standard = standards.get_road_standard("AASHTO")
traffic_standard = standards.get_traffic_standard("HCM")
