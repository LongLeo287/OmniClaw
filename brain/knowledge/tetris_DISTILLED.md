---
id: Tetris
type: knowledge
owner: OA_Triage
---
# Tetris
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: tetris.c
```c
/*
 * Tetris.c : Camillo J. Taylor Nov. 4, 2011
 */

#include "lc4libc.h"

/*
 * #############  DATA STRUCTURES THAT STORE THE GAME STATE ######################
 */

// Number of rows and columns in the tetris array
#define NROWS     15
#define NCOLS     16

#define NSHAPES    7

// Array specifying the configuration of the game pieces - for every shape there are 4 entries
// correspoinding to the 4 possible orientations. Each configuration is captured by a 16 bit field
// where each bit corresponds to a cell. The MSB corresponds to the top left cell, the next bit to the
// cell next to that etc.

lc4uint shapes[NSHAPES][4] = { 
  { 0x0660U, 0x0660U, 0x0660U, 0x0660U},
  { 0xF000U, 0x4444U, 0xF000U, 0x4444U},
  { 0x8E00U, 0x6440U, 0x0E20U, 0x44C0U},
  { 0x2E00U, 0x4460U, 0x0E80U, 0xC440U},
  { 0xC600U, 0x4C80U, 0xC600U, 0x4C80U},
  { 0x6C00U, 0x8C40U, 0x6C00U, 0x8C40U},
  { 0x4E00U, 0x4640U, 0x0E40U, 0x4C40U}
 };

// Each shape has an associated color - these colors are defined in lc4libc.h
lc4uint colors[NSHAPES] = {RED, BLUE, GREEN, YELLOW, ORANGE, CYAN, WHITE};

//Game Score
int score = 0;

// This 2D array contains the current state of the tetris array each entry indicates the color
// currently stored in the corresponding block. Zero entries indicate unoccupied blocks.
lc4uint cells[NROWS][NCOLS];
/*lc4uint cells[NROWS][NCOLS] = {
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
{WHITE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, WHITE},
{RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED, RED},
{RED, BLUE, GREEN, YELLOW, ORANGE, CYAN, RED, RED, RED, BLUE, GREEN, YELLOW, ORANGE, CYAN, WHITE, BLUE}};
*/

/*
 * ###############################################################################
 */

void print_num(lc4uint num)
{
	// Max value of num is 2**16-1=65535 which has 5 characters + 1 for null
	// Don't need space for minus sign, because number is unsigned
	char s[6];
	if (num == 0) {
		lc4_puts((lc4uint*)"0\n");
	} else {
		lc4_utoa(num, s, 6);
		lc4_puts((lc4uint*)s);
		lc4_puts((lc4uint*)"\n");
	}
}

// Clear the tetris array
void clear_tetris_array ()
{

  /// YOUR CODE HERE
	int i, j;
	for (i = 0; i < NROWS; i++)
		for (j = 0; j < NCOLS; j++)
			cells[i][j] = 0;

}

/*
 * ################# CODE FOR DRAWING THE SCENE ##########################
 */

//
// Draw the cells on the screen using the lc4_draw_8x8 routine.
// Remember to skip the top 4 rows in the display since a 15x16 array of 8x8 pixel blocks
// will take 120x128 pixels while our display has 124 rows.
//
void draw_cells ()
{
	int i, j;
	for (i = 0; i < NROWS; i++){
		for (j = 0; j < NCOLS; j++){
			lc4_draw_8x8(j*8, i*8 + 4, cells[i][j]);
		}
	}
}

void redraw ()
{
  // This function assumes that PennSim is being run in double buffered mode
  // In this mode we first clear the video memory buffer with lc4_reset_vmem,
  // then draw the scene, then call lc4_blt_vmem to swap the buffer to the screen
  // NOTE that you need to run PennSim with the following command:
  // java -jar PennSim.jar -d

  lc4_reset_vmem();

  draw_cells ();

  lc4_blt_vmem();
}

/*
 * ################# CODE FOR UPDATNG THE GAME STATE ##########################
 */

// Tests whether the pattern specified in the bitvector shape can be drawn without
// collision in the current array. If there is a collision return 1 else return 0.
// This function also tests whether any of the filled cells would be drawn outside
// the bounds of the array which would also be considered a collision.
int test_for_collision (lc4uint shape, int row, int col)
{

  /// YOUR CODE HERE
	int coll = 0, i, j;
	for (i = row; i < row + 4; i++) {
		for (j = col; j <  col + 4; j++) {
			if ((i >= NROWS || i < 0  || j < 0 || j >= NCOLS) && (shape & 0x8000U) != 0) {
				return 1;
			}
			else {
				if ((shape & 0x8000U) != 0 && cells[i][j] != 0) {
					return 1;
				}
			}
			shape = shape << 1;
		}
	}
	return coll;
}

// draw the specified shape into the array - you can assume that you have already
// called test_for_collision so there shouldn't be any illegal memory accesses.
void draw_shape (lc4uint shape, int row, int col, lc4uint color)
{
	int i, j;
	for (i = row; i < row+4; i++) {
		for (j = col; j < col+4; j++) {
			if ((shape & 0x8000U) != 0)
				cells[i][j] = color;
			shape = shape << 1;
		}
	}

}

// Iterate through the tetris array from bottom to top removing any rows that
// are completely filled.
void remove_filled_rows ()
{
  /// YOUR CODE HERE
	int i, j, k, fsum, check;
	for (i = NROWS - 1; i > -1; i--) {
		for (j = 0, fsum = 0, check = 0; j < NCOLS; j++)
			if (cells[i][j] != 0)
				fsum++;
		if (fsum == NCOLS)
			check = 1;
		if (check){
			score += 1;
			for (k = i; k > 0; k--)
				for (j = 0; j < NCOLS; j++)
					cells[k][j] = cells[k - 1][j];
			i++;
		}
		
	}
}


/*
 * ############################### MAIN FUNCTION #############################
 */


int main ()
{
  lc4uint event, collision;
  int game_started = 0;   // game mode
  int row, col, shape_idx, orientation;
  int new_row, new_col, new_orientation;
  clear_tetris_array ();
  redraw ();

  lc4_puts ((lc4uint*)"!!! Welcome to Tetris !!!\n");
  lc4_puts ((lc4uint*)"Press j to go left\n");
  lc4_puts ((lc4uint*)"Press k to go right\n");
  lc4_puts ((lc4uint*)"Press s to rotate clockwise\n");
  lc4_puts ((lc4uint*)"Press a to rotate counter-clockwise\n");

  lc4_puts ((lc4uint*)"Press space bar to start\n");

  row = -1;
  // MAIN LOOP

  while (1) {
    /// YOUR CODE HERE
	  
	  event = lc4_get_event();
	  if (!game_started && event == 0x00020) {
		  clear_tetris_array();
		  row = -1;
		  game_started = 1;
		  lc4_puts ((lc4uint*)"Game On!\n");
	  }
	  if (game_started) {
		  if (row == -1) {
			  row = 0;
			  col = lc4_rand_power2(8) + lc4_rand_power2(4) + lc4_rand_power2(2);
			  shape_idx = lc4_rand_power2(4) + lc4_rand_power2(4);
			  orientation = lc4_rand_power2(4);
			  if(test_for_collision(shape_idx, row, col)){
				  game_started = 0;
				  lc4_puts ((lc4uint*)"Score:\n");
				  print_num(score);
				  lc4_puts ((lc4uint*)"Game Over\n");
			  }
		  }
		  new_col = col;
		  new_row = row;
		  new_orientation = orientation;
		  if (event == 0x0006A) 
			  new_col = col - 1;
		  else {
			  if (event == 0x0006B)
				  new_col = col + 1;
			  else {
				  if (event == 0x00061)
					  new_orientation = (orientation - 1) & 0x3;
				  else {
					  if (event == 0x00073)
						  new_orientation = (orientation + 1) & 0x3;
					  else
						  new_row = row + 1;
				  }
			  }
		  }
		  
		  draw_shape(shapes[shape_idx][orientation], row, col, 0);
		  if (!test_for_collision(shapes[shape_idx][new_orientation], new_row, new_col)) {
			  row = new_row;
			  col = new_col;
			  orientation = new_orientation;
			  draw_shape(shapes[shape_idx][orientation], row, col, colors[shape_idx]);
		  }
		  else {
			  draw_shape(shapes[shape_idx][orientation], row, col, colors[shape_idx]);
			  if (event == 0) {
				  remove_filled_rows();
				  row = -1;
			  }
		  }
		  redraw();
	  } 
  }

  return 0;
}


```

