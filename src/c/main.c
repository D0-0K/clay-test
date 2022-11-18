#include <pebble.h>
#include "main.h"

#define ROUND PBL_IF_ROUND_ELSE(true, false)
#define ANTIALIASING true

static Window *s_window;
static Layer *s_window_layer;

static Layer *s_background_layer;
static GBitmap *image;
// A struct for our specific settings (see main.h)
ClaySettings settings;

uint8_t *bitmap_data;
int bytes_per_row;

int Background1 = 0xFFFFFF;
int Background2 = 0xAAAAAA;
int HourHandCol = 0xFF5500;
int MinHandCol = 0x555555;

// Set the correct screen height and width (checking for Pebble Time Round)
int HEIGHT = PBL_IF_RECT_ELSE(180,180);
int WIDTH = PBL_IF_RECT_ELSE(180,180);

// Set the height and width of the image
int IMAGE_HEIGHT = 180;
int IMAGE_WIDTH = 180;

static void col_schemes() {
  if(settings.col_number == 10 ) {
    Background1 = 0x0000AA;
    Background2 = 0x5555FF;
    HourHandCol = 0xFFFFFF;
    MinHandCol = 0x000055;
  } else if (settings.col_number == 9 ) {
    Background1 = 0xAA55FF;
    Background2 = 0xAAAAFF;
    HourHandCol = 0x00FFAA;
    MinHandCol = 0x005500;
  } else if (settings.col_number == 8 ) {
    Background1 = 0x5555AA;
    Background2 = 0xAAAAFF;
    HourHandCol = 0xFFFF55;
    MinHandCol = 0xFF5500;
  } else if (settings.col_number == 7 ) {
    Background1 = 0xAA0000;
    Background2 = 0xFF5555;
    HourHandCol = 0xFFFFAA;
    MinHandCol = 0x000000;
  } else if (settings.col_number == 6 ) {
    Background1 = 0xFFFFFF;
    Background2 = 0xAAFFAA;
    HourHandCol = 0xFF0055;
    MinHandCol = 0x005555;
  } else if (settings.col_number == 5 ) {
    Background1 = 0xFF5555;
    Background2 = 0xFFAAAA;
    HourHandCol = 0x55FF00;
    MinHandCol = 0x550000;
  } else if (settings.col_number == 4 ) {
    Background1 = 0xFFFFFF;
    Background2 = 0xAAAAFF;
    HourHandCol = 0x000055;
    MinHandCol = 0xFF0055;
  } else if (settings.col_number == 3 ) {
    Background1 = 0xFFFFFF;
    Background2 = 0xFFAAAA;
    HourHandCol = 0xFF0055;
    MinHandCol = 0x005555;
  } else if (settings.col_number == 2 ) {
    Background1 = 0x000000;
    Background2 = 0x555555;
    HourHandCol = 0xFFAA00;
    MinHandCol = 0xFFFFFF;
  } else if (settings.col_number == 1 ) {
    Background1 = 0xFFFFFF;
    Background2 = 0xAAAAAA;
    HourHandCol = 0xFF5500;
    MinHandCol = 0x555555;
  }
}

// Get the color of the pixel at (x,y)
GColor get_pixel_color(int x, int y){
	return (GColor){ .argb = bitmap_data[y*bytes_per_row + x] };
}

// Set the color of the pixel at (x,y) to "color"
void set_pixel_color(int x, int y, GColor color){
	bitmap_data[y*bytes_per_row + x] = color.argb;
}

// Go through pixels using a nested loop and replace old_color with new_color
void replace_colors(int pixel_width, int pixel_height, GColor old_color, GColor new_color){
  APP_LOG(APP_LOG_LEVEL_DEBUG, "Replacing Colours");
	int max_y = pixel_height; //Use 28 for just the hat
	int max_x = pixel_width;
	
	for(int y = 0; y < max_y; y++){
		for(int x = 0; x < max_x; x++){
			GColor pixel_color = get_pixel_color(x,y);
			if(gcolor_equal(pixel_color, old_color)){
			  set_pixel_color(x, y, new_color);
			}
		}
	}
}

static void col_redraw() {
  APP_LOG(APP_LOG_LEVEL_DEBUG, "Updating Colours");
	bitmap_data = gbitmap_get_data(image);
	bytes_per_row = gbitmap_get_bytes_per_row(image);

	replace_colors(IMAGE_WIDTH, IMAGE_HEIGHT, GColorWhite, GColorFromHEX(Background1));
	replace_colors(IMAGE_WIDTH, IMAGE_HEIGHT, GColorLightGray, GColorFromHEX(Background2));
}

// Initialize the default settings
static void prv_default_settings() {
    settings.col_number = 1;
}

// Read settings from persistent storage
static void prv_load_settings() {
  // Load the default settings
  prv_default_settings();
  // Read settings from persistent storage, if they exist
  persist_read_data(SETTINGS_KEY, &settings, sizeof(settings));
}

// Save the settings to persistent storage
static void prv_save_settings() {
  persist_write_data(SETTINGS_KEY, &settings, sizeof(settings));
  // Update the display based on new settings
  prv_update_display();
}

// Update the display elements
static void prv_update_display() {
  // Background color
  layer_mark_dirty(s_background_layer);
  col_schemes();
  APP_LOG(APP_LOG_LEVEL_DEBUG, "update display col redraw");
   col_redraw();
}

// Handle the response from AppMessage
static void prv_inbox_received_handler(DictionaryIterator *iter, void *context) {
    Tuple *color_t = dict_find(iter, MESSAGE_KEY_ColorNumber);
    if (color_t) {
       settings.col_number = atoi(color_t->value->cstring);
}

  // Save the new settings to persistent storage
  prv_save_settings();
}

static void background_layer_update_proc(Layer *layer, GContext *ctx) {

  APP_LOG(APP_LOG_LEVEL_DEBUG, "Background layer update proc");  

    graphics_context_set_compositing_mode(ctx, GCompOpSet);
    graphics_draw_bitmap_in_rect(ctx, image, GRect((WIDTH-IMAGE_WIDTH), HEIGHT-IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_HEIGHT));

  APP_LOG(APP_LOG_LEVEL_DEBUG, "background layer update col redraw");
   col_redraw();
}



// Window Load event
static void prv_window_load(Window *window) {
  s_window_layer = window_get_root_layer(window);
  GRect bounds = layer_get_bounds(s_window_layer);

  //Background Layer
  s_background_layer = layer_create(bounds);
  layer_add_child(s_window_layer, s_background_layer);
  layer_set_update_proc(s_background_layer, background_layer_update_proc);
  APP_LOG(APP_LOG_LEVEL_DEBUG, "Background layer added");

  APP_LOG(APP_LOG_LEVEL_DEBUG, "Window load update display");
  prv_update_display();
}

// Window Unload event
static void prv_window_unload(Window *window) {
  layer_destroy(s_background_layer);
}

static void prv_init(void) {
  prv_load_settings();


  // Listen for AppMessages
  app_message_register_inbox_received(prv_inbox_received_handler);
  app_message_open(128, 128);
  col_schemes();


  s_window = window_create();
  window_set_window_handlers(s_window, (WindowHandlers) {
    .load = prv_window_load,
    .unload = prv_window_unload,
  });

       // Change the background to fit the screen ratio
       if (ROUND) {
	image = gbitmap_create_with_resource(RESOURCE_ID_ROUND);
	} else {
        image = gbitmap_create_with_resource(RESOURCE_ID_RECT);
        }

  window_stack_push(s_window, true);
}

static void prv_deinit(void) {
  if (s_window) {
    window_destroy(s_window);
  }
}

int main(void) {
  prv_init();
  app_event_loop();
  prv_deinit();
}
