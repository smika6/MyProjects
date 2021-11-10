package GAME_ENGINE;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;

public class MapObject {
	protected int x, y;
	protected ID id;
	protected Image img;
	protected Color c;
	protected Game game;
	protected int size;
	
	public MapObject(Game g, int x, int y, ID id, Image img) {
		this.game = g;
		this.x = x;
		this.y = y;
		this.id = id;
		this.img = img;
		this.size = img.getWidth(game);
	}
	
	public MapObject(Game g, int x, int y, ID id, Color c, int size) {
		this.game = g;
		this.x = x;
		this.y = y;
		this.id = id;
		this.c = c;
		this.size = size;
	}
	
	public void tick() {
		
	}
	
	public void render(Graphics g) {
		g.setColor(c);
		g.fillRect(x, y, size, size);
	}
}
