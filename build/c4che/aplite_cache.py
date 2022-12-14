AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'aplite'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'aplite'
BUNDLE_NAME = 'clay-background.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-std=c99', '-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_COMPASS', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['aplite']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_JSON = [{u'gitHead': u'1bf6db08092ab464974d1762a953ea7cbd24efb8', u'_location': u'/pebble-clay', u'dist': {u'tarball': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'signatures': [{u'keyid': u'SHA256:jl3bwswu80PjjokCgh0o2w5c2U4LhQAE57gj9cz1kzA', u'sig': u'MEUCIFA12PX5bVibhTGVMnkJFWBxPBU/x5R6Jz2B7RvpzD2ZAiEA6HfjOjccw0U1kuU5M+yix7faMroR6wImCgOwGEIEN/Q='}], u'integrity': u'sha512-/rXxmltdW8JyohDzXINdea+d2wnFJVNFiTXfuZsKpySURZSCFMMucX9sZPZvbHnEA4xFINM4iicyhBbvY4ALfw==', u'shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}, u'_spec': u'pebble-clay', u'_npmOperationalInternal': {u'tmp': u'tmp/pebble-clay-1.0.4.tgz_1479759281024_0.1520081793423742', u'host': u'packages-12-west.internal.npmjs.com'}, u'keywords': [u'config', u'configuration', u'pebble', u'pebble-package'], u'devDependencies': {u'chai': u'^3.4.1', u'mocha': u'^2.3.4', u'through': u'^2.3.8', u'gulp-inline': u'0.0.15', u'karma-source-map-support': u'^1.1.0', u'deepcopy': u'^0.6.1', u'eslint-plugin-standard': u'^1.3.1', u'stringify': u'^3.2.0', u'gulp-insert': u'^0.5.0', u'gulp': u'^3.9.0', u'gulp-htmlmin': u'^1.3.0', u'deamdify': u'^0.2.0', u'bourbon': u'^4.2.6', u'eslint-config-pebble': u'^1.2.0', u'eslint': u'^1.5.1', u'karma-coverage': u'^0.5.3', u'watchify': u'^3.7.0', u'require-from-string': u'^1.1.0', u'gulp-sourcemaps': u'^1.6.0', u'karma-mocha': u'^0.2.1', u'sinon': u'^1.17.3', u'joi': u'^6.10.1', u'browserify': u'^13.0.0', u'sassify': u'^0.9.1', u'gulp-autoprefixer': u'^3.1.0', u'karma-mocha-reporter': u'^1.1.5', u'autoprefixer': u'^6.3.1', u'browserify-istanbul': u'^0.2.1', u'karma-threshold-reporter': u'^0.1.15', u'gulp-sass': u'^2.1.1', u'vinyl-source-stream': u'^1.1.0', u'gulp-uglify': u'^1.5.2', u'karma-chrome-launcher': u'^0.2.2', u'vinyl-buffer': u'^1.0.0', u'del': u'^2.0.2', u'karma': u'^0.13.19', u'karma-browserify': u'^5.0.1', u'tosource': u'^1.0.0', u'postcss': u'^5.0.14'}, u'_from': u'pebble-clay@latest', u'pebble': {u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'sdkVersion': u'3', u'projectType': u'package', u'resources': {u'media': []}, u'capabilities': [u'configurable']}, u'_inCache': True, u'_phantomChildren': {}, u'_args': [[u'pebble-clay', u'/home/pebble/pebble-projects/clay-background']], u'_nodeVersion': u'6.9.1', u'version': u'1.0.4', u'_resolved': u'https://registry.npmjs.org/pebble-clay/-/pebble-clay-1.0.4.tgz', u'readme': u'ERROR: No README data found!', u'homepage': u'https://github.com/pebble/clay#readme', u'_npmVersion': u'3.10.8', u'_requested': {u'name': u'pebble-clay', u'rawSpec': u'', u'raw': u'pebble-clay', u'scope': None, u'type': u'tag', u'spec': u'latest'}, u'description': u'Pebble Config Framework', u'repository': {u'url': u'git+https://github.com/pebble/clay.git', u'type': u'git'}, u'optionalDependencies': {}, u'_requiredBy': [u'/'], u'maintainers': [{u'name': u'pebble-tech', u'email': u'webteam@getpebble.com'}], u'dependencies': {}, u'scripts': {u'pebble-publish': u'npm run pebble-clean && npm run build && pebble build && pebble package publish && npm run pebble-clean', u'test-travis': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run --browsers chromeTravisCI && ./node_modules/.bin/eslint ./', u'pebble-build': u'npm run build && pebble build', u'test-debug': u'(export DEBUG=true && ./node_modules/.bin/gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --no-single-run)', u'lint': u'eslint ./', u'dev': u'gulp dev', u'build': u'gulp', u'test': u'gulp && ./node_modules/.bin/karma start ./test/karma.conf.js --single-run', u'pebble-clean': u'rm -rf tmp src/js/index.js && pebble clean'}, 'path': 'node_modules/pebble-clay/dist', u'_installable': True, u'_shrinkwrap': None, u'name': u'pebble-clay', u'license': u'MIT', u'author': {u'name': u'Pebble Technology'}, u'bugs': {u'url': u'https://github.com/pebble/clay/issues'}, u'_npmUser': {u'email': u'webteam@getpebble.com', u'name': u'pebble-tech'}, 'js_paths': ['node_modules/pebble-clay/dist/js/index.js'], u'_where': u'/home/pebble/pebble-projects/clay-background', u'_id': u'pebble-clay@1.0.4', u'_shasum': u'fdf92f0fdc770a979c06874eaa2457cc2e762344'}]
LIB_RESOURCES_JSON = {u'pebble-clay': []}
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {u'SecondTick': 10002, u'ForegroundColor': 10001, u'BackgroundColor': 10000, u'Animations': 10003}
MESSAGE_KEYS_DEFINITION = '/home/pebble/pebble-projects/clay-background/build/src/message_keys.auto.c'
MESSAGE_KEYS_HEADER = '/home/pebble/pebble-projects/clay-background/build/include/message_keys.auto.h'
MESSAGE_KEYS_JSON = '/home/pebble/pebble-projects/clay-background/build/js/message_keys.json'
NODE_PATH = '/home/pebble/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/home/pebble/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/home/pebble/.pebble-sdk/SDKs/current/sdk-core/pebble/aplite'
PEBBLE_SDK_ROOT = '/home/pebble/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['aplite', 'bw', 'rect', 'compass', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 524288, 'MAX_APP_MEMORY_SIZE': 24576, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'aplite', 'BUNDLE_BIN_DIR': 'aplite', 'BUILD_DIR': 'aplite', 'MAX_RESOURCES_SIZE_APPSTORE_2_X': 98304, 'MAX_RESOURCES_SIZE_APPSTORE': 131072, 'DEFINES': ['PBL_PLATFORM_APLITE', 'PBL_BW', 'PBL_RECT', 'PBL_COMPASS', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'aplite'
PREFIX = '/usr/local'
PROJECT_INFO = {'appKeys': {u'SecondTick': 10002, u'ForegroundColor': 10001, u'BackgroundColor': 10000, u'Animations': 10003}, u'sdkVersion': u'3', u'displayName': u'clay-background', u'uuid': u'4bbee27f-cef3-47c1-aaa1-7fdc74f73397', u'messageKeys': {u'SecondTick': 10002, u'ForegroundColor': 10001, u'BackgroundColor': 10000, u'Animations': 10003}, 'companyName': u'Dook', u'enableMultiJS': True, u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite'], u'capabilities': [u'configurable'], 'versionLabel': u'1.0', 'longName': u'clay-background', 'shortName': u'clay-background', u'watchapp': {u'watchface': True}, u'resources': {u'media': []}, 'name': u'clay-background'}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite']
RESOURCES_JSON = []
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 78
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['chalk', 'emery', 'basalt', 'diorite', 'aplite']
TARGET_PLATFORMS = ['diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1668783107
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/home/pebble/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
