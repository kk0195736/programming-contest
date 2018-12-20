#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>
#include "altera_up_avalon_audio.h"
#include "altera_up_avalon_character_lcd.h"
#include "altera_up_avalon_video_character_buffer_with_dma.h"
#include "altera_up_avalon_video_pixel_buffer_dma.h"
#include "altera_up_avalon_ps2.h"
#include "altera_up_avalon_parallel_port.h"
#include "sys/alt_stdio.h"

#define BUF_THRESHOLD 96 // 75% of 128 word buffer
#define DISPLAY_W 320
#define DISPLAY_H 240
#define CELL_WH 10
#define COLOR_BG 0x4a8b
#define COLOR_SNAKE 0x3522
#define COLOR_ENEMY 0xF
#define COLOR_FEED 0xe882

alt_up_parallel_port_dev *KEY_dev;
alt_up_char_buffer_dev *char_buffer_dev;
alt_up_pixel_buffer_dma_dev *pixel_buffer_dev;


typedef struct
{
  int x, y;
} pos;


typedef struct
{
  pos cell[800];
  int len;
} snake;

typedef struct
{
	pos cell[800];
	int len;
} enemy;


void drawCell(int x, int y, int color)
{
  alt_up_pixel_buffer_dma_draw_box(pixel_buffer_dev, x * CELL_WH, y * CELL_WH, x * CELL_WH + CELL_WH, y * CELL_WH + CELL_WH, color, 0);
}


void clearCell(int x, int y, int bgColor)
{
  alt_up_pixel_buffer_dma_draw_box(pixel_buffer_dev, x * CELL_WH, y * CELL_WH, x * CELL_WH + CELL_WH, y * CELL_WH + CELL_WH, bgColor, 0);
}


void drawBackGround()
{
  int i, j;
  for (i = 0; i < DISPLAY_W; i++)
  {
    for (j = 0; j < DISPLAY_H; j++)
    {
      drawCell(i, j, COLOR_BG);
    }
  }
}


void drawFrame()
{
  alt_up_pixel_buffer_dma_draw_line(pixel_buffer_dev, 0, 0, DISPLAY_W - 1, 0, 0xffff, 0);                         
  alt_up_pixel_buffer_dma_draw_line(pixel_buffer_dev, 0, DISPLAY_H - 1, DISPLAY_W - 1, DISPLAY_H - 1, 0xffff, 0); 
  alt_up_pixel_buffer_dma_draw_line(pixel_buffer_dev, 0, 0, 0, DISPLAY_H - 1, 0xffff, 0);                         
  alt_up_pixel_buffer_dma_draw_line(pixel_buffer_dev, DISPLAY_W - 1, 0, DISPLAY_W - 1, DISPLAY_H - 1, 0xffff, 0); 
}


void drawSnake(snake snake)
{
  int i;
  for (i = 0; i < snake.len - 1; i++)
  {
    drawCell(snake.cell[i].x, snake.cell[i].y, COLOR_SNAKE);
  }
}

void drawEnemy(enemy snake)
{
	int i;
	for (i = 0; i < snake.len - 1; i++)
	{
		drawCell(snake.cell[i].x, snake.cell[i].y, COLOR_ENEMY);
	}
}

void clearSnake(snake snake)
{
  int i;
  for (i = 0; i < snake.len - 1; i++)
  {
    int x = snake.cell[i].x;
    int y = snake.cell[i].y;
    drawCell(x, y, COLOR_BG);
  }
}

void clearEnemy(enemy snake)
{
	int i;
	for (i = 0; i < snake.len - 1; i++)
	{
		int x = snake.cell[i].x;
		int y = snake.cell[i].y;
		drawCell(x, y, COLOR_BG);
	}
}


void clearFeed(pos feed)
{
  drawCell(feed.x, feed.y, COLOR_BG);
}


void drawFeed(pos feed)
{
  drawCell(feed.x, feed.y, COLOR_FEED);
}

void drawTitleMenu()
{
	alt_up_pixel_buffer_dma_clear_screen(pixel_buffer_dev, 0);
	alt_up_char_buffer_clear(char_buffer_dev);

	alt_up_char_buffer_string(char_buffer_dev, "SNAKE GAME\0", 80 / 2 - 5, 60 / 2);

	alt_up_char_buffer_string(char_buffer_dev, "KEY1 EASY\0", 80 / 2 - 5, 60 / 2 + 14);
	alt_up_char_buffer_string(char_buffer_dev, "KEY2 NORMAL\0", 80 / 2 - 5, 60 / 2 + 17);
	alt_up_char_buffer_string(char_buffer_dev, "KEY3 HARD\0", 80 / 2 - 5, 60 / 2 + 20);
}


void drawGameOver(int score)
{
  alt_up_pixel_buffer_dma_clear_screen(pixel_buffer_dev, 0);
  alt_up_char_buffer_clear(char_buffer_dev);

  char message[20] = {'\0'};
  sprintf(message, "SCORE: %d", score);
  alt_up_char_buffer_string(char_buffer_dev, "Game Over!\0", 80 / 2 - 4, 60 / 2 - 2);
  alt_up_char_buffer_string(char_buffer_dev, message, 80 / 2 - 5, 60 / 2 + 1);
  alt_up_char_buffer_string(char_buffer_dev, "Press any KEY.\0", 80 / 2 - 7, 60 / 2 + 18);
}


void printScore(int score)
{
  char message[20] = {'\0'};
  sprintf(message, "SCORE: %d", score);
  alt_up_char_buffer_string(char_buffer_dev, message, 69, 2);
}


pos moveSnake(snake *snake, int direction)
{

  pos tail = snake->cell[snake->len - 1];

  int i;
  for (i = snake->len - 1; i >= 1; i--)
  {
    snake->cell[i] = snake->cell[i - 1];
  }


  switch (direction)
  {
  case 1:
    snake->cell[0].x++;
    break;
  case 2:
    snake->cell[0].y++;
    break;
  case 3:
    snake->cell[0].x--;
    break;
  case 4:
    snake->cell[0].y--;
    break;
  }

  return tail;
}

pos moveEnemy(enemy *snake, int direction)
{

	pos tail = snake->cell[snake->len - 1];

	int i;
	for (i = snake->len - 1; i >= 1; i--)
	{
		snake->cell[i] = snake->cell[i - 1];
	}


	switch (direction)
	{
	case 1:
		snake->cell[0].x++;
		break;
	case 2:
		snake->cell[0].y++;
		break;
	case 3:
		snake->cell[0].x--;
		break;
	case 4:
		snake->cell[0].y--;
		break;
	}

	return tail;
}


void growSnake(snake *snake, pos tail)
{
  snake->cell[snake->len] = tail;

  snake->len++;
}

void growEnemy(enemy *snake, pos tail)
{
	snake->cell[snake->len] = tail;

	snake->len++;
}


int isGameOver(snake snake)
{
  if (snake.cell[0].x < 0 || snake.cell[0].y < 0)
  {
    return 1;
  }

  if (snake.cell[0].x >= DISPLAY_W / CELL_WH || snake.cell[0].y >= DISPLAY_H / CELL_WH)
  {
    return 1;
  }


  int i;
  for (i = 1; i < snake.len; i++)
  {
    if (snake.cell[0].x == snake.cell[i].x && snake.cell[0].y == snake.cell[i].y)
    {
      return 1;
    }
  }

  return 0;
}

int isGameOverHard(snake snake, enemy enemy)
{
	if (snake.cell[0].x < 0 || snake.cell[0].y < 0)
	{
		return 1;
	}

	if (snake.cell[0].x >= DISPLAY_W / CELL_WH || snake.cell[0].y >= DISPLAY_H / CELL_WH)
	{
		return 1;
	}


	int i;
	for (i = 1; i < snake.len; i++)
	{
		if (snake.cell[0].x == snake.cell[i].x && snake.cell[0].y == snake.cell[i].y)
		{
			return 1;
		}
	}
	for (i = 1; i < enemy.len; i++)
	{
		if (snake.cell[0].x == enemy.cell[i].x && snake.cell[0].y == enemy.cell[i].y)
		{
			return 1;
		}
	}

	return 0;
}


int isGetFeed(snake snake, pos feed)
{
  if (snake.cell[0].x == feed.x && snake.cell[0].y == feed.y)
  {
    return 1;
  }

  return 0;
}

int isGetFeedEnemy(enemy snake, pos feed)
{
	if (snake.cell[0].x == feed.x && snake.cell[0].y == feed.y)
	{
		return 1;
	}

	return 0;
}


int getInputKey(alt_up_parallel_port_dev *KEY_dev)
{
  int KEY_value = alt_up_parallel_port_read_data(KEY_dev);
  int xor = 0x0 ^ KEY_value;
  int hd = 0; 
  while (xor)
  {
    xor &= xor-1;
    hd++;
  }
  if (hd > 1)
  { 
    return 0;
  }

  return KEY_value;
}


pos newFeed()
{
  srand(time(NULL));
  int x = rand() % (DISPLAY_W / CELL_WH);
  int y = rand() % (DISPLAY_H / CELL_WH);
  pos feed = {x, y};

  return feed;
}

int main(void)
{
	while (1) {

		pixel_buffer_dev = alt_up_pixel_buffer_dma_open_dev("/dev/VGA_Pixel_Buffer");


		char_buffer_dev = alt_up_char_buffer_open_dev("/dev/VGA_Char_Buffer");


		KEY_dev = alt_up_parallel_port_open_dev("/dev/Pushbuttons");


		alt_up_char_buffer_clear(char_buffer_dev);


		alt_up_pixel_buffer_dma_clear_screen(pixel_buffer_dev, 0);

		int gameMode = 1;


		drawTitleMenu();
		usleep(500000);
		while (1)
		{

			int KEY_value = getInputKey(KEY_dev);
			if (KEY_value)
			{
				if (KEY_value == 8)
				{
					gameMode = 1;
				}
				if (KEY_value == 4)
				{
					gameMode = 2;
				}
				if (KEY_value == 2)
				{
					gameMode = 3;
				}
				alt_up_char_buffer_clear(char_buffer_dev);
				break;
			}
		}

		drawBackGround();

		int direction = 2;
		int score = 0;
		int speed = 0;

		if (gameMode == 1)
		{
			speed = 100000;
		}
		else if (gameMode == 2)
		{
			speed = 200000;
		}
		else
		{
			speed = 400000;
		}

		snake snake = {
			{{14, 12},
			 {13, 12},
			 {12, 12},
			 {11, 12}},
			4 };

		pos tail;
		pos feed = newFeed();

		if (gameMode == 1) {
			int enemyDirection = 2;
			enemy enemy = {
				{ { 30, 4 },
			{ 30, 3 },
			{ 30, 2 },
			{ 30, 1 } },
			4 };

			pos enemyTail;

			while (1)
			{
				drawFeed(feed);
				drawSnake(snake);
				drawEnemy(enemy);
				drawFrame();
				printScore(score);

				usleep(speed);

				int KEY_value = getInputKey(KEY_dev);
				if (KEY_value)
				{
					if (KEY_value == 8)
					{
						if (direction != 1)
						{
							direction--;
						}
						else
						{
							direction = 4;
						}
					}
					if (KEY_value == 4)
					{
						if (direction != 4)
						{
							direction++;
						}
						else
						{
							direction = 1;
						}
					}
				}
				if (enemy.cell[0].x == 0) {
					if (enemyDirection == 3) {
						if (enemy.cell[0].y >= 12) {
							enemyDirection = 4;
						}
						else {
							enemyDirection = 2;
						}
					}

					else if (enemyDirection == 2 | enemyDirection == 4) {
						enemyDirection = 1;
					}
				}
				if (enemy.cell[0].x == 31) {
					if (enemyDirection == 1) {
						if (enemy.cell[0].y >= 12) {
							enemyDirection = 4;
						}
						else {
							enemyDirection = 2;
						}
					}

					else if (enemyDirection == 2 | enemyDirection == 4) {
						enemyDirection = 3;
					}
				}
				if (enemy.cell[0].y == 0) {
					if (enemyDirection == 4) {
						if (enemy.cell[0].x >= 16) {
							enemyDirection = 3;
						}
						else {
							enemyDirection = 1;
						}
					}

					else if (enemyDirection == 1 | enemyDirection == 3) {
						enemyDirection = 2;
					}
				}
				if (enemy.cell[0].y == 23) {
					if (enemyDirection == 2) {
						if (enemy.cell[0].x >= 16) {
							enemyDirection = 3;
						}
						else {
							enemyDirection = 1;
						}
					}

					else if (enemyDirection == 1 | enemyDirection == 3) {
						enemyDirection = 4;
					}
				}
				

				clearSnake(snake);
				clearEnemy(enemy);
				tail = moveSnake(&snake, direction);
				enemyTail = moveEnemy(&enemy, enemyDirection);

				if (isGameOverHard(snake, enemy))
				{
					break;
				}

				if (isGetFeed(snake, feed))
				{
					growSnake(&snake, tail);
					clearFeed(feed);
					feed = newFeed();
					score = score + 100;
				}
				if (isGetFeedEnemy(enemy, feed))
				{
					growEnemy(&enemy, enemyTail);
					clearFeed(feed);
					feed = newFeed();
				}
			}
		}
		else {
			while (1)
			{
				drawFeed(feed);
				drawSnake(snake);
				drawFrame();
				printScore(score);

				usleep(speed);

				int KEY_value = getInputKey(KEY_dev);
				if (KEY_value)
				{
					if (KEY_value == 8)
					{
						if (direction != 1)
						{
							direction--;
						}
						else
						{
							direction = 4;
						}
					}
					if (KEY_value == 4)
					{
						if (direction != 4)
						{
							direction++;
						}
						else
						{
							direction = 1;
						}
					}
				}

				clearSnake(snake);
				tail = moveSnake(&snake, direction);

				if (isGameOver(snake))
				{
					break;
				}

				if (isGetFeed(snake, feed))
				{
					growSnake(&snake, tail);
					clearFeed(feed);
					feed = newFeed();
					score = score + 100;
				}
			}
		}

		drawGameOver(score);
		usleep(500000);

		while (1) {
			int KEY_value = getInputKey(KEY_dev);
			if (KEY_value)
			{
				break;
			}
		}
	}

  return 0;
}
