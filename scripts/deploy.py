import config
import base

def make_desktop():
  base_dir = base.get_script_dir() + "/../out"
  core_dir = base.get_script_dir() + "/../../core"
  git_dir = base.get_script_dir() + "/../.."
  branding = base.get_env("PUBLISHER_NAME")
  if ("" == branding):
    branding = "onlyoffice"

  is_windows = True if "windows" == base.host_platform() else False  

  platforms = config.option("platform").split()
  for native_platform in platforms:
    if not native_platform in config.platforms:
      continue

    root_dir += ("/" + native_platform + "/" + branding + ("/DesktopEditors" if is_windows else "/desktopeditors")
    base.create_dir(root_dir)

    # check platform on xp
    platform = native_platform
    checkWindowsXP = platform.find("_xp")
    if (-1 != checkWindowsXP):
      platform = platform[0:checkWindowsXP]

    apps_postfix = platform
    if (-1 != checkWindowsXP):
      apps_postfix += "_xp"

    base.create_dir(root_dir + "/converter")	  
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "UnicodeConverter")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "graphics")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "PdfWriter")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "PdfReader")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "DjVuFile")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "XpsFile")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "HtmlFile")
	  base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "HtmlRenderer")

	  if ("ios" == platform):
      base.copy_lib(core_dir + "/build/lib/" + platform, root_dir + "/converter", "x2t")
    else:
      base.copy_exe(core_dir + "/build/bin/" + platform, root_dir + "/converter", "x2t")

    if (0 == platform.find("win")):
      base.copy_file(core_dir + "/Common/3dParty/icu/" + platform + "/build/icudt58.dll", root_dir + "/converter/icudt58.dll")
      base.copy_file(core_dir + "/Common/3dParty/icu/" + platform + "/build/icuuc58.dll", root_dir + "/converter/icuuc58.dll")

    if (0 == platform.find("linux")):
      base.copy_file(core_dir + "/Common/3dParty/icu/" + platform + "/build/libicudata.so.58", root_dir + "/converter/libicudata.so.58")
      base.copy_file(core_dir + "/Common/3dParty/icu/" + platform + "/build/libicuuc.so.58", root_dir + "/converter/libicuuc.so.58")

    if (0 == platform.find("mac")):
      base.copy_file(core_dir + "/Common/3dParty/icu/" + platform + "/build/libicudata.58.dylib", root_dir + "/converter/libicudata.58.dylib")
      base.copy_file(core_dir + "/Common/3dParty/icu/" + platform + "/build/libicuuc.58.dylib", root_dir + "/converter/libicuuc.58.dylib")

    if (-1 != checkWindowsXP):
      base.copy_lib(core_dir + "/core/build/lib/" + platform + "/xp", root_dir + "/converter", "doctrenderer")
      base.copy_files(core_dir + "/Common/3dParty/v8/v8_xp/" + platform + "/release/icudt*.dll", root_dir + "/converter/")
    else:
      base.copy_lib(core_dir + "/core/build/lib/" + platform, root_dir + "/converter", "doctrenderer")
      if (0 == platform.find("win")):
        base.copy_files(core_dir + "/Common/3dParty/v8/v8/out.gn/" + platform + "/release/icudt*.dat", root_dir + "/converter/")
      else:
        base.copy_file(core_dir + "/Common/3dParty/v8/v8/out.gn/" + platform + "/release/icudtl.dat", root_dir + "/converter/icudtl.dat")

    base.copy_file(git_dir + "/desktop-apps/common/converter/DoctRenderer.config", root_dir + "/converter/DoctRenderer.config")
    base.copy_dir(git_dir + "/desktop-apps/common/converter/empty", root_dir + "/converter/empty")

    if (-1 == checkWindowsXP) and (0 != platform.find("mac")) and (0 != platform.find("ios")):
      base.copy_exe(core_dir + "/build/lib/" + platform, root_dir, "HtmlFileInternal")

	  base.copy_dir(git_dir + "/dictionaries", root_dir + "/dictionaries")
    base.delete_dir(root_dir + "/dictionaries/.git")

    base.copy_dir(git_dir + "/desktop-apps/common/package/fonts", root_dir + "/fonts")
    base.copy_file(git_dir + "/desktop-apps/common/package/license/3dparty/3DPARTYLICENSE", root_dir + "/3DPARTYLICENSE")
  
    if (-1 == checkWindowsXP):
      base.copy_files(core_dir + "core/Common/3dParty/cef/" + platform + "/build/*", root_dir + "/")
    elif (native_platform == "win_64_xp"):
      base.copy_files(core_dir + "core/Common/3dParty/cef/winxp_64/build/*", root_dir + "/")
    else:
      base.copy_files(core_dir + "core/Common/3dParty/cef/winxp_32/build/*", root_dir + "/")

    isUseQt = True
    if (0 == platform.find("mac")) or (0 == platform.find("ios")):
      isUseQt = False

    if (0 == platform.find("mac")):
      base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "hunspell")
      base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "ooxmlsignature")
      base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "ascdocumentscore")
      base.copy_dir(core_dir + "/build/lib/" + platform + "/ONLYOFFICE Helper.app", root_dir + "/ONLYOFFICE Helper.app")

    if isUseQt:
      base.copy_qt_lib("Qt5Core", root_dir)
      base.copy_qt_lib("Qt5Gui", root_dir)
      base.copy_qt_lib("Qt5PrintSupport", root_dir)
      base.copy_qt_lib("Qt5Svg", root_dir)
      base.copy_qt_lib("Qt5Widgets", root_dir)
      base.copy_qt_lib("Qt5Multimedia", root_dir)
      base.copy_qt_lib("Qt5MultimediaWidgets", root_dir)
      base.copy_qt_lib("Qt5Network", root_dir)
      base.copy_qt_lib("Qt5OpenGL", root_dir)

      base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "hunspell")
      base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "ooxmlsignature")

      if (-1 != checkWindowsXP):
        base.copy_lib(core_dir + "/build/lib/" + platform + "/xp", root_dir, "ascdocumentscore")
        base.copy_lib(core_dir + "/build/lib/" + platform + "/xp", root_dir, "videoplayer")
      else:
        base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "ascdocumentscore")
        base.copy_lib(core_dir + "/build/lib/" + platform, root_dir, "videoplayer")

      base.copy_qt_plugin("bearer", root_dir)
      base.copy_qt_plugin("iconengines", root_dir)
      base.copy_qt_plugin("imageformats", root_dir)
      base.copy_qt_plugin("platforms", root_dir)
      base.copy_qt_plugin("platforminputcontexts", root_dir)
      base.copy_qt_plugin("printsupport", root_dir)
      base.copy_qt_plugin("mediaservice", root_dir)
      base.copy_qt_plugin("playlistformats", root_dir)

      base.copy_qt_plugin("platformthemes", root_dir)
      base.copy_qt_plugin("xcbglintegrations", root_dir)

      base.copy_qt_plugin("styles", root_dir)

      if (0 == platform.find("linux")):
        base.copy_qt_icu(root_dir)
        base.copy_qt_lib("Qt5DBus", root_dir)
        base.copy_qt_lib("Qt5X11Extras", root_dir)
        base.copy_qt_lib("Qt5XcbQpa", root_dir)
        base.copy_files(base.get_env("QT_DEPLOY") + "/../lib/libqgsttools_p.so*", root_dir)

      if (0 == platform.find("win")):
        base.copy_file(git_dir + "/desktop-apps/win-linux/extras/projicons/projicons_" + apps_postfix + ".exe", root_dir + "/DesktopEditors.exe")
        base.copy_file(git_dir + "/desktop-apps/win-linux/DesktopEditors_" + apps_postfix + ".exe", root_dir + "/editors.exe")
        base.copy_file(git_dir + "desktop-apps/win-linux/res/icons/desktopeditors.ico", root_dir + "/app.ico")
      elif (0 == platform.find("linux")):
        base.copy_file(git_dir + "/desktop-apps/win-linux/DesktopEditors_" + apps_postfix, root_dir + "/DesktopEditors")

      base.create_dir(root_dir + "/editors")
      base.copy_dir(base_dir + "/js/desktop/sdkjs", root_dir + "/editors/sdkjs")
      base.copy_dir(base_dir + "/js/desktop/web-apps", root_dir + "/editors/web-apps")

      base.create_dir(root_dir + "/editors/sdkjs-plugins")
      base.copy_file(git_dir + "/sdkjs-plugins/LICENSE.txt", root_dir + "/editors/sdkjs-plugins/LICENSE.txt")
      base.copy_file(git_dir + "/sdkjs-plugins/README.md", root_dir + "editors/sdkjs-plugins/README.md")
      base.copy_file(git_dir + "/sdkjs-plugins/plugins.css", root_dir + "/editors/sdkjs-plugins/plugins.css")
      base.copy_file(git_dir + "/sdkjs-plugins/pluginBase.js", root_dir + "/editors/sdkjs-plugins/pluginBase.js")

      base.copy_dir(git_dir + "/sdkjs-plugins/youtube", root_dir + "/editors/sdkjs-plugins/{38E022EA-AD92-45FC-B22B-49DF39746DB4}")
      base.copy_dir(git_dir + "/sdkjs-plugins/ocr", root_dir + "/editors/sdkjs-plugins/{440EBF13-9B19-4BD8-8621-05200E58140B}")
      base.copy_dir(git_dir + "/sdkjs-plugins/translate", root_dir + "/editors/sdkjs-plugins/{7327FC95-16DA-41D9-9AF2-0E7F449F687D}")
      base.copy_dir(git_dir + "/sdkjs-plugins/synonim", root_dir + "/editors/sdkjs-plugins/{BE5CBF95-C0AD-4842-B157-AC40FEDD9840}")
      base.copy_dir(git_dir + "/sdkjs-plugins/code", root_dir + "/editors/sdkjs-plugins/{BE5CBF95-C0AD-4842-B157-AC40FEDD9841}")
      base.copy_dir(git_dir + "/sdkjs-plugins/photoeditor", root_dir + "/editors/sdkjs-plugins/{07FD8DFA-DFE0-4089-AL24-0730933CC80A}")
      base.copy_dir(git_dir + "/sdkjs-plugins/macros", root_dir + "/editors/sdkjs-plugins/{E6978D28-0441-4BD7-8346-82FAD68BCA3B}")

      base.copy_dir(git_dir + "/desktop-sdk/ChromiumBasedEditors/plugins/{8D67F3C5-7736-4BAE-A0F2-8C7127DC4BB8}", root_dir + "/editors/sdkjs-plugins/{8D67F3C5-7736-4BAE-A0F2-8C7127DC4BB8}")
      base.copy_dir(git_dir + "/desktop-sdk/ChromiumBasedEditors/plugins/encrypt/ui/common/{14A8FC87-8E26-4216-B34E-F27F053B2EC4}", root_dir + "/editors/sdkjs-plugins/{14A8FC87-8E26-4216-B34E-F27F053B2EC4}")
      base.copy_dir(git_dir + "/desktop-sdk/ChromiumBasedEditors/plugins/encrypt/ui/engine/blockchain/{B17BDC61-59FC-41A7-A471-CD2C415A665E}", root_dir + "/editors/sdkjs-plugins/{B17BDC61-59FC-41A7-A471-CD2C415A665E}")

      if (0 != platform.find("mac")):
        base.copy_dir(git_dir + "/desktop-sdk/ChromiumBasedEditors/plugins/{060E6A7D-2766-44E8-A0EE-9A8CB9DB00D1}", root_dir + "/editors/sdkjs-plugins/{060E6A7D-2766-44E8-A0EE-9A8CB9DB00D1}")
        base.copy_dir(git_dir + "/desktop-sdk/ChromiumBasedEditors/plugins/{B509123E-6335-40BD-B965-91EB799346E3}", root_dir + "/editors/sdkjs-plugins/{B509123E-6335-40BD-B965-91EB799346E3}")
        base.copy_dir(git_dir + "/desktop-sdk/ChromiumBasedEditors/plugins/{F7E59EB4-317E-4E0B-AB2C-58E038A59EE2}", root_dir + "/editors/sdkjs-plugins/{F7E59EB4-317E-4E0B-AB2C-58E038A59EE2}")

      base.copy_file(base_dir + "/js/desktop/index.html", root_dir + "/index.html")
      base.copy_file(git_dir + "/desktop-apps/common/loginpage/addon/externalcloud.json", root_dir + "/editors/externalcloud.json")

      if (0 == platform.find("win")):
        base.copy_lib(git_dir + "/desktop-apps/win-linux/3dparty/WinSparkle", root_dir, "WinSparkle")
        base.delete_file(root_dir + "/cef_sandbox.lib")
        base.delete_file(root_dir + "/libcef.lib")

      # all themes generate ----
      base.copy_exe(core_dir + "/build/bin/" + platform, root_dir + "/converter", "allfontsgen")
      base.copy_exe(core_dir + "/build/bin/" + platform, root_dir + "/converter", "allthemesgen")

      env_cmd = ""
      if (0 == platform.find("linux")):
        env_cmd = "LD_LIBRARY_PATH=" + root_dir + "/converter"
      elif (0 == platform.find("mac")):
        env_cmd = "DYLD_LIBRARY_PATH=" + root_dir + "/converter"

      exe_ext = ".exe" if (0 == platform.find("win")) else ""
      base.cmd(env_cmd + " " + root_dir + "/converter/allfontsgen" + exe_ext, ["--use-system=\"1\"", "--input=\"" + root_dir + "/fonts" + "\"", "--allfonts=\"" + root_dir + "/converter/AllFonts.js" + "\"", "--selection=\"" + root_dir + "/converter/font_selection.bin" + "\""])
      base.cmd(env_cmd + " " + root_dir + "/converter/allthemesgen" + exe_ext, ["--converter-dir=\"" + root_dir + "/converter" + "\"", "--src=\"" + root_dir + "/editors/sdkjs/slide/themes" + "\"", "--allfonts=\"AllFonts.js\""])

      base.delete_file(root_dir + "/converter/allfontsgen" + exe_ext)
      base.delete_file(root_dir + "/converter/allthemesgen" + exe_ext)
      base.delete_file(root_dir + "/converter/AllFonts.js")
      base.delete_file(root_dir + "/converter/font_selection.bin")
      base.delete_file(root_dir + "/editors/sdkjs/slide/sdk-all.cache")

  return

def make_builder():
  return

def make():
  if config.check_option("module", "desktop"):
    make_desktop()
  if config.check_option("module", "builder"):
    make_builder()
  return