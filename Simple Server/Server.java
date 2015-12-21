import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;

import java.net.Socket;
import java.net.ServerSocket;

import java.util.ArrayList;

public class Server {

  public static void main(String[] arguments) throws Exception {

    // we are going to construct a ServerSocket that will listen on port 8080.
    ServerSocket serverSocket = new ServerSocket(8080);
    Socket clientConnection = null;
    String browser = new String();
    
    do {
    
	  ArrayList<String> parameters = new ArrayList<String>();
   	  ArrayList<String> values = new ArrayList<String>();
    
      // this call will block until a client tries to connect.
      clientConnection = serverSocket.accept();
      
      // if you open your browser and go to http://localhost:8080/ this program will receive the
      // request.
      InputStream in = clientConnection.getInputStream();
      BufferedReader reader = new BufferedReader(new InputStreamReader(in));
      
      // we'll use the code below to read the HTTP Request line-by-line.
      String line = reader.readLine();
      while (line != null && !line.equals("")) {
        // we'll output each line to the console so you can see what the HTTP request looks like.
        System.out.println(line);
        
        //Get the GET Request's parameters and values
        if(line.matches("^[GET].*$")){
        	line = line.substring(5);
        	String[] requests = line.split("\\?|&|\\s");
        	for(String request : requests){
        		if(request != null && request.length() > 0){
        			if(request.contains("=")){
        				String[] paramvalue = request.split("=");
        				parameters.add(paramvalue[0]);
        				values.add(paramvalue[1]);
        			}
        			else{
        			    parameters.add(request);
        				values.add("None");
        			}	
        		}
        	} 
        }
        
        // Browser detection using User-Agent isnt the most reliable so I used this site as a referenece: 
        // https://developer.mozilla.org/en-US/docs/Browser_detection_using_the_user_agent
        else if(line.matches("^User-Agent.*$")){
        
            if(line.contains("Firefox") && !line.contains("Seamonkey")) { browser = "Firefox"; }
        		
        	else if(line.contains("Seamonkey")) { browser = "Seamonkey"; }
        	
        	else if(line.contains("MSIE")) { browser = "Internet Explorer"; }
        	
        	else if(line.contains("Opera") || line.contains("OPR")) { browser = "Opera"; }
        	
            else if(line.contains("Chrome") && !line.contains("Chromium")) { browser = "Chrome"; }
        	
        	else if(line.contains("Chromium")) { browser = "Chromium"; }
        	
        	else if(line.contains("Safari") && (!line.contains("Chrome") && !line.contains("Chromium")) ) { browser = "Safari"; }
        }
        
        line = reader.readLine();
      }
      
      // this code will write a basic HTTP Response
      OutputStreamWriter out = new OutputStreamWriter(clientConnection.getOutputStream());
      out.write("HTTP/1.1 200 OK\n");
      out.write("Content-Type: text/html; charset=utf-8\n\n");
      out.write("<html><body>");
      out.write("THIS IS A RESPONSE<br>");
      out.write("Hello, I am Christian Boni<br>");
      out.write("<br>GET Requests:<br>");
    
      System.out.println(parameters.size());
      
      for(int i = 0; i < parameters.size(); i++){
      	out.write("Parameter: ");
      	out.write(parameters.get(i));
      	out.write(" Value: ");
      	out.write(values.get(i));
      	out.write("<br>");
      }
      
      out.write("<br>Your browser is: " + browser);
      out.write("</body></html>");
    
      out.close();
    
    } while (clientConnection != null);
  }
}
