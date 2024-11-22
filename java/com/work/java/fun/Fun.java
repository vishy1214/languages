package fun;

import java.nio.charset.Charset;
import java.util.Random;

public class Fun {
    private static Fun funEvent = null;

    public static Fun getFunEvent(){ //creates a singleton object
        return (funEvent == null)? new Fun(): funEvent;
    }

    public static Fun newFunEvent(){  //not a singleton
        return new Fun();
    }

    public void printEventName(){
        byte[] bytes = new byte[7];
        new Random().nextBytes(bytes);
        System.out.println(new String(bytes,Charset.forName("UTF-8")));
    }


}


