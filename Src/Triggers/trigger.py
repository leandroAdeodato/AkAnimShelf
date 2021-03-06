# -*- coding: utf-8 -*-
"""
=============================================================================
MODULE: trigger.py
-----------------------------------------------------------------------------
This is an intermidiate module that triggers all the user actions. It is the
module responsible for communicating with the GUI using the signal/slots
mechanism. That´s the module that need to be imported when the user defines
a hotkey.
-----------------------------------------------------------------------------
USAGE:
# GO TO THE NEXT FRAME (Default Hotkey: X)
from AkAnimShelf.Src.Triggers import trigger as trg
trg.Trigger().go_to_the_next_frame()
-----------------------------------------------------------------------------
AUTHOR:   Leandro Adeodato
VERSION:  v1.0.0 | Maya 2022 | Python 3
=============================================================================
"""
import maya.cmds as cmd
from PySide2 import QtCore as cor

from AkAnimShelf.Src.Core.Playback.PlaybackTools import playback_tools as pbt
from AkAnimShelf.Src.Core.Playback.FrameMarker import frame_marker as fmk
from AkAnimShelf.Src.Core.Keyframing.GraphEditor import graph_editor as grp
from AkAnimShelf.Src.Core.Navigation import transform_modes as trs
from AkAnimShelf.Src.Data import user_data as data
from AkAnimShelf.Src.Utils import info_utils as info
from AkAnimShelf.Src.Utils import maya_widgets_utils as mwu

MOVE, ROTATE, SCALE = 'Move', 'Rotate', 'Scale'
MODIFIER = 'Control', 'Alt', 'Shift'
BASE_LAYER, DEFAULT_LAYER = 'BaseAnimation', 'layer001'
NONE, CTRL, ALT, SHIFT = 0, 1, 2, 3
RED, GREEN, BLUE, YELLOW, PINK, ORANGE = 12, 18, 17, 21, 19, 20
KEY, BREAKDOWN, INBETWEEN = 0, 1, 2
TIME_CONTROL_OBJ = "$gPlayBackSlider"

global AK_FRAME_MARKER

class Trigger(cor.QObject):
    info_sent = cor.Signal(str)
    coordinate_system_changed = cor.Signal(list)
    transform_mode_changed = cor.Signal(str)
    camera_zoom_changed = cor.Signal(float)
    camera_hpan_changed = cor.Signal(float)
    camera_vpan_changed = cor.Signal(float)
    frame_markers = None

    def __init__(self):
        super(Trigger, self).__init__()

        self._playback_tools = pbt.PlaybackTools()
        self._frame_marker = fmk.FrameMarker()
        self._graph_editor = grp.GraphEditor()
        self._transform_modes = trs.TransformModes()
        self._selected_channels = []
        self._colors = [RED, GREEN, BLUE, YELLOW, PINK, ORANGE]

    # =========================================================================
    # SUPRESS SCRIPT EDITOR_INFO
    # =========================================================================
    def supress_script_editor_info(self, state=True):
        cmd.scriptEditorInfo(suppressInfo=state, suppressErros=state, suppressWarnings=state)

    # =========================================================================
    # TOGGLE MOVE MODE
    # =========================================================================
    def toggle_move_mode(self):
        self.supress_script_editor_info(True)
        current_mode = self._transform_modes.toggle_move_mode()
        info.show_message('Move Mode: {0}'.format(current_mode))
        self.supress_script_editor_info(False)

    # =========================================================================
    # TOGGLE ROTATE MODE
    # =========================================================================
    def toggle_rotate_mode(self):
        self.supress_script_editor_info(True)
        current_mode = self._transform_modes.toggle_rotate_mode()
        info.show_message('Rotate Mode: {0}'.format(current_mode))
        self.supress_script_editor_info(False)

    # =========================================================================
    # TOGGLE ROTATE MODE
    # =========================================================================
    def toggle_scale_mode(self):
        self.supress_script_editor_info(True)
        current_mode = self._transform_modes.toggle_scale_mode()
        info.show_message('Scale Mode: {0}'.format(current_mode))
        self.supress_script_editor_info(False)

    # ============================================================================= #
    # SLICE CURVES                                                                  #
    # ============================================================================= #
    def smart_key(self):
        print('smart_key')
        info.show_message('Smart Key')
        data.UserData().read_data()
        self._graph_editor.smart_key()

    # =========================================================================
    # COMMON TOOLS TRIGGER
    # =========================================================================
    # def switch_manipulator_mode(self, modifier=None):
    #     self._common_tools.switch_manipulator_mode()
    #
    # def toggle_move_mode(self, modifier=None):
    #     result = self._common_tools.toggle_move_mode()
    #     self.info_sent.emit('> Move Mode: {0}'.format(result))
    #     self.transform_mode_changed.emit(result)
    #
    # def toggle_rotate_mode(self, modifier=None):
    #     result = self._common_tools.toggle_rotate_mode()
    #     self.info_sent.emit('> Rotate Mode: {0}'.format(result))
    #     self.transform_mode_changed.emit(result)
    #
    # def toggle_scale_mode(self, modifier=None):
    #     result = self._common_tools.toggle_scale_mode()
    #     self.info_sent.emit('> Scale Mode: {0}'.format(result))
    #     self.transform_mode_changed.emit(result)
    #
    # def toggle_translate_channels(self, modifier=None):
    #     self._selected_channels = self._common_tools.toggle_translate_channels(modifier)
    #     self.info_sent.emit('> Toogle Translate Channels')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def toggle_rotate_channels(self, modifier=None):
    #     self._selected_channels = self._common_tools.toggle_rotate_channels(modifier)
    #     self.info_sent.emit('> Toogle Rotate Channels')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def toggle_scale_channels(self, modifier=None):
    #     self._selected_channels = self._common_tools.toggle_scale_channels(modifier)
    #     self.info_sent.emit('> Toogle Scale Channels')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def toggle_all_channels(self, modifier=None):
    #     self._common_tools.toggle_all_channels(modifier)
    #     self.info_sent.emit('> Toggle All Channels')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def select_all_channels(self, modifier=None):
    #     self._selected_channels = self._common_tools.select_all_channels(modifier)
    #     self.info_sent.emit('> All channels selected')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def clear_all_channels(self, modifier=None):
    #     self._selected_channels = self._common_tools.clear_all_channels(modifier)
    #     self.info_sent.emit('> Channels cleared')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def activate_sync_mode(self, modifier, state):
    #     self._selected_channels = self._common_tools.activate_sync_mode(modifier, state)
    #     self.info_sent.emit('> Channels cleared')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def set_anim_mode(self, modifier=None):
    #     self._selected_channels = self._common_tools.set_anim_mode(modifier)
    #     self.info_sent.emit('> Channels cleared')
    #     self.coordinate_system_changed.emit(self._selected_channels)
    #
    # def set_previs_mode(self, modifier=None):
    #     self._selected_channels = self._common_tools.set_previs_mode(modifier)
    #     self.info_sent.emit('> Channels cleared')
    #     self.coordinate_system_changed.emit(self._selected_channels)

    # =========================================================================
    # KEYFRAMING TOOLS TRIGGER
    # =========================================================================
    # def pull_keys_back(self, modifier=None):
    #     print('pull_keys_back')
    #
    # def nudge_key_back(self, modifier=None):
    #     print('nudge_key_back')
    #
    # def nudge_key_forward(self, modifier=None):
    #     print('nudge_key_forward')
    #
    # def push_keys_forward(self, modifier=None):
    #     print('push_keys_forward')
    #
    # def copy_keys(self, modifier=None):
    #     print('copy_keys')
    #
    # def cut_keys(self, modifier=None):
    #     print('cut_keys')
    #
    # def insert_keys(self, modifier=None):
    #     print('insert_keys')
    #
    # def replace_keys(self, modifier=None):
    #     print('replace_keys')
    #
    # def bake_on_ones(self, modifier=None):
    #     print('bake_on_ones')
    #
    # def bake_on_twos(self, modifier=None):
    #     print('bake_on_twos')
    #
    # def bake_on_fours(self, modifier=None):
    #     print('bake_on_fours')
    #
    # def bake_on_markers(self, modifier=None):
    #     print('bake_on_markers')
    #
    # def bake_on_shared_keys(self, modifier=None):
    #     print('bake_on_shared_keys')
    #
    # def bake_on_base_layer_keys(self, modifier=None):
    #     print('bake_on_base_layer_keys')
    #
    # def store_selected_keytimes(self, modifier=None):
    #     print('store_selected_keytimes')
    #
    # def bake_on_stored_keytimes(self, modifier=None):
    #     print('bake_on_stored_keytimes')

    # =========================================================================
    # SELECTION TOOLS TRIGGER
    # =========================================================================
    # def next_left_control(self, modifier=None):
    #     self._selector.next_right_control(modifier)
    #
    # def next_up_control(self, modifier=None):
    #     print('next_up_control')
    #     self._selector.next_up_control(modifier)
    #
    # def next_down_control(self, modifier=None):
    #     print('next_down_control')
    #     self._selector.next_down_control(modifier)
    #
    # def next_right_control(self, modifier=None):
    #     print('next_right_control')
    #     self._selector.next_left_control(modifier)
    #
    # def select_all_set(self, modifier=None):
    #     print('select_all_set')
    #
    # def select_upperbody_set(self, modifier=None):
    #     print('select_upperbody_set')
    #
    # def select_right_hand_set(self, modifier=None):
    #     print('select_right_hand_set')
    #
    # def select_left_hand_set(self, modifier=None):
    #     print('select_left_hand_set')
    #
    # def select_right_arm_set(self, modifier=None):
    #     print('select_right_arm_set')
    #
    # def select_left_arm_set(self, modifier=None):
    #     print('select_left_arm_set')
    #
    # def select_right_leg_set(self, modifier=None):
    #     print('select_right_leg_set')
    #
    # def select_left_leg_set(self, modifier=None):
    #     print('select_left_leg_set')

    # =========================================================================
    # TRANSFORM TOOLS TRIGGER
    # =========================================================================
    # def toggle_move_all_mode(self, modifier=None):
    #     print('toggle_move_all_mode')
    #
    # def toggle_ik_mover(self, modifier=None):
    #     print('toggle_ik_mover')
    #
    # def change_pivot(self, modifier=None):
    #     print('change_pivot')
    #
    # def micro_transform(self, modifier=None):
    #     print('micro_transform')
    #
    # def increase_transform(self, modifier=None):
    #     print('increase_transform')
    #
    # def decrease_transform(self, modifier=None):
    #     print('decrease_transform')
    #
    # def reset_transforms(self, modifier=None):
    #     print('reset_transforms')
    #
    # def snap_locator(self, modifier=None):
    #     print('snap_locator')
    #
    # def copy_transforms(self, modifier=None):
    #     print('copy_transforms')
    #
    # def paste_transforms(self, modifier=None):
    #     print('paste_transforms')
    #
    # def align_transforms(self, modifier=None):
    #     print('align_transforms')
    #
    # def mirror_transforms(self, modifier=None):
    #     print('mirror_transforms')
    #
    # def transfer_xform(self, modifier=None):
    #     print('transfer_xform')
    #
    # def flexible_constraints(self, modifier=None):
    #     print('flexible_constraints')
    #
    # def rotate_character_base(self, modifier=None):
    #     print('rotate_character_base')
    #
    # def rotate_character_pose(self, modifier=None):
    #     print('rotate_character_pose')
    #
    # def snap_character_base(self, modifier=None):
    #     print('snap_character_base')
    #
    # def snap_character_pose(self, modifier=None):
    #     print('snap_character_pose')
    #
    # def copy_relationship(self, modifier=None):
    #     print('copy_relationship')
    #
    # def paste_relationship(self, modifier=None):
    #     print('paste_relationship')
    #
    # def reload_relationship(self, modifier=None):
    #     print('reload_relationship')
    #
    # def remove_relationship(self, modifier=None):
    #     print('remove_relationship')

    # =========================================================================
    # VIEWPORT TOOLS TRIGGER
    # =========================================================================
    # def toggle_viewport_mode(self, modifier=None):
    #     print('toggle_viewport_mode')
    #
    # def toggle_shot_cameras(self, modifier=None):
    #     print('toggle_shot_cameras')
    #
    # def toggle_workspace(self, modifier=None):
    #     print('toggle_workspace')
    #
    # def toggle_layout_mode(self, modifier=None):
    #     print('toggle_layout_mode')
    #
    # def toggle_hotkey_set(self, modifier=None):
    #     print('toggle_hotkey_set')
    #
    # def toggle_expert_mode(self, modifier=None):
    #     print('toggle_expert_mode')
    #
    # def filter_objects_visibility(self, modifier=None):
    #     print('filter_objects_visibility')
    #
    # def toggle_ortographic_views(self, modifier=None):
    #     print('toggle_ortographic_views')
    #
    # def toggle_image_plane_visibility(self, modifier=None):
    #     print('toggle_image_plane_visibility')
    #
    # def set_image_plane_to_blocking(self, modifier=None):
    #     print('set_image_plane_to_blocking')
    #
    # def create_image_plane(self, modifier=None):
    #     print('create_image_plane')
    #
    # def remove_image_plane(self, modifier=None):
    #     print('remove_image_plane')
    #
    # def cinematic_editor(self, modifier=None):
    #     print('cinematic_editor')
    #
    # def camera_noise_editor(self, modifier=None):
    #     print('camera_noise_editor')
    #
    # def tracker_tool(self, modifier=None):
    #     print('tracker_tool')
    #
    # def snapshot_tool(self, modifier=None):
    #     print('snapshot_tool')
    #
    # def get_camera_panzoom_attrs(self, camera):
    #     return self._viewport_tools.get_camera_panzoom_attrs(camera)
    #     print('get_camera_panzoom_attrs')
    #
    # def set_camera_panzoom_attrs(self, camera, values):
    #     print('set_camera_panzoom_attrs')

    # =========================================================================
    # GO TO THE NEXT FRAME
    # =========================================================================
    def go_to_the_next_frame(self, modifier=None):
        self.supress_script_editor_info(True)
        self._playback_tools.go_to_the_next_frame()
        info.show_message('Next Frame >>')
        self.supress_script_editor_info(False)

    # =========================================================================
    # GO TO THE PREV FRAME
    # =========================================================================
    def go_to_the_prev_frame(self, modifier=None):
        self.supress_script_editor_info(True)
        self._playback_tools.go_to_the_prev_frame()
        info.show_message('<< Previous Frame')
        self.supress_script_editor_info(False)

    # =========================================================================
    # GO TO THE NEXT KEY
    # =========================================================================
    def go_to_the_next_key(self, modifier=None):
        self.supress_script_editor_info(True)
        self._playback_tools.go_to_the_next_key()
        info.show_message('Next Key >>')
        self.supress_script_editor_info(False)

    # =========================================================================
    # GO TO THE PREV FRAME
    # =========================================================================
    def go_to_the_prev_key(self, modifier=None):
        self.supress_script_editor_info(True)
        self._playback_tools.go_to_the_prev_key()
        info.show_message('<< Previous Key')
        self.supress_script_editor_info(False)

    def next_frame_playback_press(self, modifier=None):
        self._playback_tools.next_frame_playback_press()

    def next_frame_playback_release(self, modifier=None):
        self._playback_tools.next_frame_playback_release()

    def prev_frame_playback_press(self, modifier=None):
        self._playback_tools.prev_frame_playback_press()

    def prev_frame_playback_release(self, modifier=None):
        self._playback_tools.prev_frame_playback_release()

    def playback(self, modifier=None):
        print('playback')

    def play(self, modifier=None):
        print('play')

    def start_frame(self, modifier=None):
        print('start_frame')

    # =========================================================================
    # LOAD FRAME MARKERS
    # =========================================================================
    def load_frame_markers(self):
        self.supress_script_editor_info(True)
        info.show_message('Frame Markers Loaded')
        global AK_FRAME_MARKER

        try:
            AK_FRAME_MARKER.setParent(None)
            AK_FRAME_MARKER.deleteLater()
            AK_FRAME_MARKER = None
        except:
            pass

        parent = mwu.MayaWidgetsUtils.get_maya_control(TIME_CONTROL_OBJ)
        AK_FRAME_MARKER = fmk.FrameMarker()
        AK_FRAME_MARKER.setVisible(True)
        self.supress_script_editor_info(False)

    # =========================================================================
    # ADD FRAME MARKERS
    # =========================================================================
    def add_frame_markers(self, type):
        self.supress_script_editor_info(True)
        info.show_message('Frame Marker Added')
        AK_FRAME_MARKER.add_frame_markers(type)
        self.supress_script_editor_info(False)

    # =========================================================================
    # REMOVE FRAME MARKERS
    # =========================================================================
    def remove_frame_markers(self):
        self.supress_script_editor_info(True)
        info.show_message('Frame Marker Removed')
        AK_FRAME_MARKER.remove_frame_markers()
        self.supress_script_editor_info(False)

    # =========================================================================
    # CLEAR ALL FRAME MARKERS
    # =========================================================================
    def clear_all_frame_markers(self):
        self.supress_script_editor_info(True)
        info.show_message('Frame Markers Cleared')
        AK_FRAME_MARKER.clear_all_frame_markers()
        self.supress_script_editor_info(False)

    # # ============================================================================= #
    # # LIST MARKER KEYTIMES                                                          #
    # # ============================================================================= #
    # def list_markers_keytimes(self, marker_type):
    #     print('list_marker_keytimes')
    #     self._playback_tools.list_markers_keytimes()

    # # ============================================================================= #
    # # SHARE KEYS ON MARKERS                                                         #
    # # ============================================================================= #
    # def share_keys_on_markers(self, marker_type):
    #     print('share_keys_on_markers')
    #     self._playback_tools.share_keys_on_markers()

    # # ============================================================================= #
    # # GO TO THE NEXT MARKER                                                         #
    # # ============================================================================= #
    # def go_to_the_next_marker(self, marker_type):
    #     print('go_to_the_next_marker')
    #     self._playback_tools.go_to_the_next_marker()

    # def end_frame(self, modifier=None):
    #     print('end_frame')
    #
    # def prev_marker(self, modifier=None):
    #     print('prev_marker')
    #
    # def prev_shot(self, modifier=None):
    #     print('prev_shot')
    #
    # def next_shot(self, modifier=None):
    #     print('next_shot')
    #
    # def next_marker(self, modifier=None):
    #     print('next_marker')
    #
    # def swap_shot_left(self, modifier=None):
    #     print('swap_shot_left')
    #
    # def prev_base_layer_key(self, modifier=None):
    #     print('prev_base_layer_key')
    #
    # def next_base_layer_key(self, modifier=None):
    #     print('next_base_layer_key')
    #
    # def swap_shot_right(self, modifier=None):
    #     print('swap_shot_right')
    #
    # def crop_timeline_left(self, modifier=None):
    #     print('crop_timeline_left')
    #     self._playback_tools.crop_timeline_left()
    #     self.info_sent.emit('> Crop Timeline Left')
    #
    # def move_start_time_to_current_frame(self, modifier=None):
    #     print('move_start_time_to_current_frame')
    #     self._playback_tools.move_start_time_to_current_frame()
    #     self.info_sent.emit('> Move Start Time to Current Frame')
    #
    # def move_end_time_to_current_frame(self, modifier=None):
    #     print('move_end_time_to_current_frame')
    #     self._playback_tools.move_end_time_to_current_frame()
    #     self.info_sent.emit('> Move End Time to Current Frame')
    #
    # def crop_timeline_right(self, modifier=None):
    #     print('crop_timeline_left')
    #     self._playback_tools.crop_timeline_right()
    #     self.info_sent.emit('> Crop Timeline Right')
    #
    # def frame_prev_section(self, modifier=None):
    #     print('frame_prev_section')
    #
    # def center_cursor_to_range(self, modifier=None):
    #     print('center_cursor_to_range')
    #     self._playback_tools.center_cursor_to_range()
    #     self.info_sent.emit('> Center Cursor to Range')
    #
    # def center_range_to_cursor(self, modifier=None):
    #     print('center_range_to_cursor')
    #     self._playback_tools.center_range_to_cursor()
    #     self.info_sent.emit('> Center Range to Cursor')
    #
    # def frame_next_section(self, modifier=None):
    #     print('frame_next_section')

    # =========================================================================
    # CHANNEL BOX
    # =========================================================================

    # =========================================================================
    # TIMELINE
    # =========================================================================

    # =========================================================================
    # GRAPH EDITOR
    # =========================================================================
    # def toggle_infinity(self, modifier=None):
    #     print('toggle_infinity')
    #
    # def toggle_buffer_curves(self, modifier=None):
    #     print('toggle_buffer_curves')
    #
    # def toggle_curves_view_mode(self, modifier=None):
    #     print('toggle_curves_view_mode')
    #
    # def toggle_pre_infinity_cycle_mode(self, modifier=None):
    #     print('toggle_pre_infinity_cycle_mode')
    #
    # def toggle_post_infinity_cycle_mode(self, modifier=None):
    #     print('toggle_post_infinity_cycle_mode')
    #
    # def toggle_mute_selected_channels_(self, modifier=None):
    #     print('toggle_mute_selected_channels_')
    #
    # def toggle_lock_selected_channels_(self, modifier=None):
    #     print('toggle_lock_selected_channels_')
    #
    # def toggle_buffer_selected_channels_(self, modifier=None):
    #     print('toggle_buffer_selected_channels_')
    #
    # def toggle_break_unify_tangents(self, modifier=None):
    #     print('toggle_break_unify_tangents')
    #
    # def toggle_free_lock_tangents(self, modifier=None):
    #     print('toggle_free_locked_tangents')
    #
    # def add_smart_key(self, modifier=None):
    #     print('add_smart_key')
    #
    # def add_breakdown_key(self, modifier=None):
    #     print('add_breakdown_key')
    #
    # def toggle_isolate_selection(self, modifier=None):
    #     print('toggle_isolate_selection')
    #
    # def toggle_tangent_types(self, modifier=None):
    #     print('toggle_isolate_selection')

    # =========================================================================
    # LAYERS
    # =========================================================================
    # def create_new_anim_layer(self, modifier=None, layer=DEFAULT_LAYER):
    #     print('create_new_anim_layer')
    #     self._layer_tools.create_new_anim_layer(layer)
    #
    # def delete_selected_anim_layers(self, modifier=None):
    #     print('delete_selected_anim_layers')
    #     self._layer_tools.delete_selected_anim_layers()
    #
    # def set_active_anim_layer(self, layer=BASE_LAYER, modifier=None):
    #     print('set_active_anim_layer')
    #     self._layer_tools.set_active_anim_layer(layer)
    #
    # def set_anim_layers_color(self, layer=BASE_LAYER, color=None, modifier=None):
    #     print('set_anim_layers_color')
    #     if color is None:
    #         self._layer_tools.set_active_anim_layer(layer, self._colors[RED])
    #     else:
    #         self._layer_tools.set_active_anim_layer(layer, color)
    #
    #
    # def merge_selected_anim_layers(self, modifier=None):
    #     print('merge_selected_layers')
    #
    # def lock_anim_layers(self, modifier=None):
    #     print('lock_layers')
    #
    # def solo_anim_layers(self, modifier=None):
    #     print('solo_layers')
    #
    # def mute_anim_layers(self, modifier=None):
    #     print('mute_layers')
    #
    # def select_anim_layers(self, modifier=None):
    #     print('mute_layers')
    #
    #
    #
    # def activate_next_anim_layer(self, modifier=None):
    #     print('activate_next_layer')
    #
    # def activate_prev_anim_layer(self, modifier=None):
    #     print('activate_prev_layer')
    #
    # def set_anim_layers_color(self, modifier=None):
    #     print('set_layers_color')

    # =========================================================================
    # PREFERENCES MANAGER
    # =========================================================================
    # def toggle_hotkey_sets(self, modifier=None):
    #     print('toggle_hotkey_sets')
    #
    # def toggle_workspaces(self, modifier=None):
    #     print('toggle_workspaces')
    #
    # def toggle_expert_mode(self, modifier=None):
    #     print('toggle_expert_mode')











