import utils
from mirror_coordinates import centered_x, centered_y
from config import geom

geometry = "geometries/ideal-frame-mirrorbox-support1.yaml"

mir_len_x = geom.mirror_array.mirror_dimensions.x  # mirror x dimension
mir_len_y = geom.mirror_array.mirror_dimensions.y

abs_len_x = geom.absorber.dimensions.x
abs_len_y = geom.absorber.dimensions.y

abs_pos_x = geom.absorber.position.x
abs_pos_y = geom.absorber.position.y

box_space_x = geom.mirror_box.space.x
box_space_y = geom.mirror_box.space.y
box_height = geom.mirror_box.height

top_len_x = geom.top_cover.dimensions.x
top_len_y = geom.top_cover.dimensions.y


def append_reflectors_to_yaml(fpath):
    """ Appends reflectors to yaml as entities """
    utils.keep_until(fpath, occurrence='reflector', lines_before=1)
    count = 1
    with open(fpath, 'a') as f:
        for x in centered_x:
            for y in centered_y:
                reflector = f"- entity:\n    name: reflector{count}\n" \
                            f"    transform: {{ rotation: [0 ,0, 0], " \
                            f"translation: [ {x:.3f}, 0, {y:.3f} ] }}\n" \
                            "    children: [ *self_oriented_facet ]\n\n"
                f.writelines(reflector)
                count += 1


def move_absorber(geometry, abs_pos_x, abs_pos_y):
    abs_transform = f"    transform: {{ rotation: [90, 0, 0], " \
                    f"translation: [&abs_x {abs_pos_x}, 1.5, &abs_y {abs_pos_y}] }}\n"
    utils.replace_line(geometry, newline=abs_transform)
    if "support" in geometry:
        set_horizontal_support_vertices(geometry, abs_len_x, abs_len_y,
                                        abs_pos_x, abs_pos_y)


def add_mirrorbox(geometry):
    box_h = box_height / 2
    box_z = centered_x[-1] + mir_len_x / 2 + box_space_x
    box_z_h = f"            - [ &box_z {box_z},        *box_h]\n"
    box_z_neg = f"            - [ &box_z_neg {-box_z},   &box_h_neg {-box_h}]\n"
    box_h_pos = f"            - [ *box_z_neg,         &box_h {box_h}]\n"
    utils.replace_line(geometry, occurrence="&box_z ", newline=box_z_h)
    utils.replace_line(geometry, occurrence="&box_z_neg", newline=box_z_neg)
    utils.replace_line(geometry, occurrence="&box_h ", newline=box_h_pos)

    box_x = centered_y[-1] + mir_len_y / 2 + box_space_y
    box_x_pos = f"            - [ &box_x {box_x},       *box_h]\n"
    box_x_neg = f"            - [ &box_x_neg {-box_x},  *box_h_neg]\n"
    utils.replace_line(geometry, occurrence="&box_x ", newline=box_x_pos)
    utils.replace_line(geometry, occurrence="&box_x_neg ", newline=box_x_neg)


def set_vertices(geometry, name, len_x, len_y):
    x = len_x / 2
    y = len_y / 2
    vertices = f"          vertices: {name}\n" \
               f"           - [{-x}, {-y}]\n" \
               f"           - [{-x},  {y}]\n" \
               f"           - [ {x},  {y}]\n" \
               f"           - [ {x}, {-y}]\n"
    utils.replace_occurence_and_four_next(geometry,
                                          occurrence=name,
                                          newlines=vertices)


def set_horizontal_support_vertices(geometry, len_x, len_y, abs_x, abs_y):
    x = len_x / 2
    y = len_y / 2
    name = "&absorber_support_horizontal_vertices"
    vertices = f"            vertices: &absorber_support_horizontal_vertices\n" \
               f"             - [{-x}, -0.506]\n" \
               f"             - [ {-x + abs_x},  {-y + abs_y}]\n" \
               f"             - [ {x + abs_x},  {-y + abs_y}]\n" \
               f"             - [ {x}, -0.506]\n"
    utils.replace_occurence_and_four_next(geometry,
                                          occurrence=name,
                                          newlines=vertices)


def setup_base_geometry(geometry):
    set_vertices(geometry, "&mirror_vertices", mir_len_x, mir_len_y)
    set_vertices(geometry, "&receiver_vertices", abs_len_x, abs_len_y)
    set_vertices(geometry, "&absorber_top_cover_vertices", top_len_x, top_len_y)
    add_mirrorbox(geometry)
    append_reflectors_to_yaml(geometry)
    move_absorber(geometry, abs_pos_x, abs_pos_y)


setup_base_geometry(geometry)
# move_absorber(geometry, 0.5, 0.5)
