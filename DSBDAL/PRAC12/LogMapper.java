import java.io.IOException;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;

public class LogMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    private final static IntWritable one = new IntWritable(1);
    private Text logLevel = new Text();

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] parts = line.split("\\s+");
        if (parts.length > 2 && parts[2].matches(".*\\[.*\\].*")) {
            String level = parts[2].replaceAll("\\[|\\]", "");
            logLevel.set(level);
            context.write(logLevel, one);
        }
    }
}

