package GAME_ENGINE;
import java.awt.Color;
import java.awt.Graphics;
import GAME_ENGINE.Game.STATE;
/**
 * Write a description of class HUD here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class HUD{
	private Game game;
    public static long startTime; 
    private long stopTime, endTime;
    private static boolean takeTime = true;
    private static float HEALTH = 100;
    private float gVal = 200;
    public HUD(Game game){
        takeTime = true;
        startTime = System.nanoTime();
        HEALTH = 100;
        this.game = game;
    }

    public void tick(){
        HEALTH= AuxFunctions.clamp(HEALTH,0,100);
        gVal = HEALTH*2;
    }

    public void render(Graphics g){
        stopTime = System.nanoTime();
        g.setColor(Color.gray);
        g.fillRect(15,15, 200,32);
        g.setColor(new Color((int)(200-gVal),(int)gVal,0));
        g.fillRect(15,15, (int)HEALTH*2,32);
        g.setColor(Color.white);
        g.drawRect(15,15, 200,32);
        g.drawString("Health: " + (int)HEALTH + "/100",17,27);
        g.drawString("Seconds: " + (stopTime-startTime)/1000000000, 80, 10);
        if(game.getState() == STATE.Game){
            if(HEALTH<=0){
                if(takeTime){
                    endTime = System.nanoTime();
                    takeTime = false;
                }
                g.drawRect(70,85,225,60);
                g.drawString("Your Seconds on Run: " + (endTime-startTime)/1000000000, 75, 100);
                g.drawString("!!!PRESS M TO RETURN TO MENU!!!", 75, 135);
            }
        }
    }
    
    public static float getHealth() {
    	return HEALTH;
    }
    
    public static void add2Health(float hp) {
    	HEALTH+=hp;
    }
    
    public static void takeTime() {
    	takeTime = !takeTime;
    }
    
}
