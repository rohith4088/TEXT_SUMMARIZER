package com.example.exp9;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import org.json.JSONArray;
import org.json.JSONObject;
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.w3c.dom.Element;
import java.io.InputStream;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.nio.charset.StandardCharsets;
public class MainActivity extends AppCompatActivity {

    TextView display;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
       display = findViewById(R.id.textView2);
    }
    public void parsexml(View v){
        try {
            InputStream is = getAssets().open("city.xml");
            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
            DocumentBuilder db = dbf.newDocumentBuilder();
            Document doc = db.parse(is);
            StringBuilder sb = new StringBuilder();
            sb.append("XML DATA");
            sb.append("\n------------");
            NodeList nl = doc.getElementsByTagName("place");
            for(int i = 0;i<nl.getLength();i++){
                Node node = nl.item(i);
                if(node.getNodeType() == Node.ELEMENT_NODE){
                    Element el = (Element) node;
                    sb.append("\nname").append(getValue("name",el));
                    sb.append("\nlatitude").append(getValue("lat",el));
                    sb.append("\nlatitude").append(getValue("lon",el));
                    sb.append("\nlatitude").append(getValue("temp",el));
                    sb.append("\nlatitude").append(getValue("hum",el));

                }
            }
            display.setText(sb.toString());
        }
        catch (Exception e){
            e.printStackTrace();
        }

    }
    public void parsejson(View v){
        String json;
        StringBuilder sb = new StringBuilder();
        try{
            InputStream is = getAssets().open("city.json");
            int size = is.available();
            byte[] buffer = new byte[size];
            is.read(buffer);
            json = new String(buffer,StandardCharsets.UTF_8);
            JSONArray ja = new JSONArray(json);
            sb.append("JSON DATA");
            sb.append("\n_----------");
            for (int i = 0;i<ja.length();i++){
                JSONObject jo = ja.getJSONObject(i);
                sb.append("\n name").append(jo.getString("name"));
                sb.append("\n name").append(jo.getString("name"));
                sb.append("\n name").append(jo.getString("name"));
                sb.append("\n name").append(jo.getString("name"));
                sb.append("\n name").append(jo.getString("name"));


            }
            display.setText(sb.toString());
            is.close();
        }
        catch(Exception e){
            e.printStackTrace();
        }

        }
        private String getValue(String tag , Element el){
        return el.getElementsByTagName(tag).item(0).getChildNodes().item(0).getNodeValue();
    }
}