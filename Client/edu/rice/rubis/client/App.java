package edu.rice.rubis.client;

import org.apache.kafka.clients.producer.*;
import org.apache.kafka.common.serialization.LongSerializer;
import org.apache.kafka.common.serialization.StringSerializer;
import java.util.Properties;

public class App 
{	
	private final static String TOPIC = "responsetime";
    private final static String BOOTSTRAP_SERVERS ="172.25.130.9:9092";
    
	
    public Producer<String, String> createProducer() {
        Properties props = new Properties();
        props.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG,
                                            BOOTSTRAP_SERVERS);
        props.put(ProducerConfig.CLIENT_ID_CONFIG, "KafkaRubisProducer");
        props.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG,
                                        StringSerializer.class.getName());
        props.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG,
                                    StringSerializer.class.getName());
        return new KafkaProducer<>(props);
    }
    
    public void runProducer(Producer<String, String> producer, final String key, final String msg) throws Exception {
        
        try {
                final ProducerRecord<String, String> record =
                        new ProducerRecord<>(TOPIC, key, msg);
						
                RecordMetadata metadata = producer.send(record).get();
				
               // System.out.printf("sent record(key=%s value=%s) ",
                        //record.key(), record.value());
            
			} 
			finally {
				producer.flush();
			}
    }
    
    public static void main(String... args) throws Exception {
		
    }
}
