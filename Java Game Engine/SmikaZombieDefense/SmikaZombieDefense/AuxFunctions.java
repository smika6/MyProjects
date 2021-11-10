 

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
    public static float distance(float x1, float y1, float x2, float y2) {
    	return((float)Math.sqrt(Math.pow((x2-x1), 2)+Math.pow((y2-y1), 2)));
    }
}
