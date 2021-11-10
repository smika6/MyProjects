package GAME_ENGINE;

public class AuxFunctions {
    public static float clamp(float var, float min, float max){
        if(var>=max){
            return var = max;
        }else if(var <= min){
            return var=min;
        }else{
            return var;
        }
    }
}
