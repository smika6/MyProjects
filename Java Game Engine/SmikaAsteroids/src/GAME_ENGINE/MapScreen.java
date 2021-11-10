package GAME_ENGINE;

import java.awt.Color;
import java.awt.Graphics;
import java.util.Random;

public class MapScreen {
	private Game game;
	private int blockWidth = 25;
	private int rows = (int)game.HEIGHT/blockWidth;
	private int cols = (int)game.WIDTH/blockWidth;
	private MapObject[][] map;
	private Random r = new Random();
	
	public MapScreen(Game g) {
		this.game = g;
		map = new MapObject[cols][rows];
		//System.out.println(rows + " " + cols + " " + cols*blockWidth);
	}
	
	public void tick() {
		for(int i = 0; i < cols; i++) {
			for(int j = 0; j<rows; j++) {
				map[i][j].tick();
			}
		}
	}
	
	public void render(Graphics g) {
		for(int i = 0; i < cols; i++) {
			for(int j = 0; j<rows; j++) {
				map[i][j].render(g);
			}
		}
	}
	
	public void generateRandomMap() {
		for(int i = 0; i < cols; i++) {
			for(int j = 0; j<rows; j++) {
				if(r.nextInt(10)>2) {
					map[i][j] = new MapObject(game, i*blockWidth, j*blockWidth, ID.Ground, new Color(r.nextInt(255),r.nextInt(255),r.nextInt(255)), blockWidth);
				}else {
					map[i][j] = new MapObject(game, i*blockWidth, j*blockWidth, ID.Wall, new Color(r.nextInt(255),r.nextInt(255),r.nextInt(255)), blockWidth);

				}
			}
		}
	}
	
	public void generateCheckeredMap() {
		for(int i = 0; i < cols; i++) {
			for(int j = 0; j<rows; j++) {
				if((i+j)%2==0) {
					map[i][j] = new MapObject(game, i*blockWidth, j*blockWidth, ID.Ground, new Color(51,51,51), blockWidth);
				}else {
					map[i][j] = new MapObject(game, i*blockWidth, j*blockWidth, ID.Wall, new Color(0,0,0), blockWidth);

				}
			}
		}
	}
	
	
	
}
