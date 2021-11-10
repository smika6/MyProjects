package GAME_ENGINE;
import java.awt.Color;
import java.awt.Graphics;
import java.util.Scanner;
import GAME_ENGINE.Game.STATE;
/**
 * Write a description of class HUD here.
 *
 * @author Jacob Hopkins
 * @version v1.0
 */
public class HUD{
    public static long startTime; 
    public long stopTime, endTime;
    public static boolean takeTime = true;
    public static float HEALTH = 80;
    private float gVal = 200;
    public static float score = 0;
    public static float level = 0, highest = 0;
    public HUD(){
        score = 0;
        level = 0;
        takeTime = true;
        startTime = System.nanoTime();
        HEALTH = 80;
        highest = 0;
    }

    public void tick(){
        HEALTH= Game.clamp(HEALTH,0,100);
        gVal = HEALTH*2;
        if(HEALTH>0){
            score++;
        }
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
        g.drawString("Level: " + level, 17, 60);
        g.drawString("Score: " + Spawn.scoreKeep, 17, 70);
        g.drawString("Seconds: " + (stopTime-startTime)/1000000000, 17, 80);
        if(Game.gameState == STATE.Game){
            if(HEALTH<=0){
                if(takeTime){
                    endTime = System.nanoTime();
                    highest=level;
                    takeTime = false;
                }
                g.drawRect(70,85,225,60);
                g.drawString("Your Seconds on Run: " + (endTime-startTime)/1000000000, 75, 100);
                g.drawString("Your Score: " + (int)score, 75, 110);
                g.drawString("Your Level: " + highest, 75, 120);
                g.drawString("!!!PRESS M TO RETURN TO MENU!!!", 75, 135);
            }
        }
    }

    public void setScore(int score){
        this.score = score;
    }

    public float getScore(){
        return score;
    }

    public void setLevel(float level){
        this.level = level;
    }

    public float getLevel(){
        return level;
    }
}
