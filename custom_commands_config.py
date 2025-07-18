"""
ملف الأوامر المخصصة - يتم إنشاؤه تلقائياً بواسطة مصنع الأوامر
تم آخر تحديث: 2025-06-22 21:49:55
"""

CUSTOM_COMMANDS_DATA = {   'dance_commands': [   {   'command': 'منور',
                              'created_at': '2025-06-21T14:22:03.424777',
                              'emote': 'emote-bow',
                              'enabled': True,
                              'id': 1,
                              'message': '،',
                              'permissions': 'everyone'},
                          {   'auto_repeat': True,
                              'command': 'ممل',
                              'created_at': '2025-06-21T14:29:35.656880',
                              'emote': 'idle-posh',
                              'enabled': True,
                              'id': 2,
                              'is_auto_dance': True,
                              'message': 'تم',
                              'permissions': 'everyone',
                              'updated_at': '2025-06-22T12:55:57.265517'},
                          {   'command': 'سوجا',
                              'created_at': '2025-06-21T21:52:41.986442',
                              'emote': 'emote-maniac',
                              'enabled': True,
                              'id': 3,
                              'message': '^^',
                              'permissions': 'everyone'},
                          {   'command': 'تو',
                              'created_at': '2025-06-21T22:05:24.780614',
                              'emote': 'emote-bow',
                              'enabled': True,
                              'id': 4,
                              'message': '_',
                              'permissions': 'everyone'},
                          {   'command': 'خناقة',
                              'created_at': '2025-06-21T22:07:30.488813',
                              'emote': 'idle-fighter',
                              'enabled': True,
                              'id': 5,
                              'message': '^^',
                              'permissions': 'everyone'},
                          {   'auto_repeat': True,
                              'command': 'جوست',
                              'created_at': '2025-06-21T22:14:16.575583',
                              'emote': 'emote-ghost-idle',
                              'enabled': True,
                              'id': 6,
                              'is_auto_dance': True,
                              'message': '،',
                              'permissions': 'everyone',
                              'updated_at': '2025-06-22T12:54:28.397153'},
                          {   'auto_repeat': True,
                              'command': 'سيت',
                              'created_at': '2025-06-22T13:01:17.081930',
                              'emote': 'sit-open',
                              'enabled': True,
                              'id': 7,
                              'is_auto_dance': True,
                              'message': '🕺💃',
                              'permissions': 'everyone',
                              'updated_at': '2025-06-22T13:01:21.536146'},
                          {   'auto_repeat': True,
                              'command': 'طيرني',
                              'created_at': '2025-06-22T21:49:50.666045',
                              'emote': 'idle-floating',
                              'enabled': True,
                              'id': 8,
                              'is_auto_dance': True,
                              'message': '🕺💃',
                              'permissions': 'everyone',
                              'updated_at': '2025-06-22T21:49:55.065085'}],
    'message_commands': [],
    'navigation_commands': [   {   'command': 'متوسط',
                                   'coordinates': {   'x': 4.0,
                                                      'y': 7.0,
                                                      'z': 4.0},
                                   'created_at': '2025-06-22T21:48:30.929731',
                                   'enabled': True,
                                   'id': 1,
                                   'message': '',
                                   'permissions': 'everyone'}],
    'settings': {   'created_at': '2025-06-21T12:28:42.470505',
                    'enabled': True,
                    'version': '1.0'},
    'teleport_commands': []}

def get_navigation_commands():
    """الحصول على أوامر التنقل"""
    return CUSTOM_COMMANDS_DATA.get("navigation_commands", [])

def get_all_custom_commands():
    """الحصول على جميع الأوامر المخصصة"""
    return CUSTOM_COMMANDS_DATA

def is_custom_command(command_text):
    """فحص إذا كان النص أمر مخصص"""
    nav_commands = get_navigation_commands()
    for cmd in nav_commands:
        if cmd.get("enabled", True) and cmd.get("command", "").lower() == command_text.lower():
            return True, cmd
    return False, None
