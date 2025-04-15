# Rideau Canal Skateway Real-Time Monitoring System: A Data-Driven Safety Solution  

## Project Context  
The iconic Rideau Canal Skateway, a celebrated winter attraction in Ottawa, faces operational difficulties due to fluctuating ice conditions affected by climate change. Ensuring public safety is the key responsibility for the National Capital Commission (NCC), A robust monitoring system needs to operate with responsiveness in order to address this need. Real-time data monitoring for the canal represents a vital project which supports decision-making about opening and closure operations that protect skating safety. 

## Solution to the Problem  
This issue can be solved by regularly monitoring various aspects of the canal using IoT Sensors which can be placed all around the canal to measure the following:  

Public safety from falling into the canal is determined by measuring ice thickness in centimeters.  
The ice melting risks increase when surface temperatures reach Celsius values.  
The measurement of snow accumulation in centimeters determines the ice structure since excessive snow prevents public skating.  
The external temperature measured in Celsius helps indicate whether canal ice skating can proceed.  

## Architecture Diagram of the System
![image](https://github.com/user-attachments/assets/3ae07bf0-b32d-4165-889c-921ca9fe766a)  
The provided diagram demonstrates the connection between IoT devices and Azure Cloud services. The IoT devices send their data through connection strings to IoT hub before Azure Stream Analytics performs processing operations. The completed processed data is directed to Azure Blob storage where it resides in specific containers.  

## Implementation of the model  
The first step included creating simulated IoT sensors through software. The development achieved its goal by embracing Python scripts and .env files for managing secure virtual device connections through environment variables. This segment shows how to get and apply IoT connection information through this sample code:  
![image](https://github.com/user-attachments/assets/ee3ec847-0d31-4374-833c-577d0f54c4c2)  

The code block of simulated sensor reading generation appears inside the main function. The main function runs continuously to replicate the ongoing canal observation process. The system produces randomly generated realistic values of ice thickness, surface temperature, snow accumulation and external temperature for each point on the skateway locations (Dow's Lake, Fifth Avenue, NAC).  
![image](https://github.com/user-attachments/assets/8bc96ee1-b16e-428c-873f-a2d5dab74592)  
The JSON format structures the gathered measurements which are presented in the following code lines. The JSON data accompanied by its designated index is sent to the sendToIotHub() function which transports the information to Azure IoT Hub endpoints. Each sensor data transmission gets deliberately delayed by a 10-second interval to replicate actual reporting periods.

## Setting Up Azure IoT Hub  
IOT Hub supports Azure as the base component for cloud infrastructure. Setting up an IoT Hub instance under the free tier became the starting point for portal configuration to handle expenditure. The system received public access for network connections and maintained default security protocols. Three IoT devices were then set up inside the hub to represent sensors located at different canal points.  

The steps to establish individual IoT devices within the hub appear in the following illustration. Each simulated sensor required a digital identity to be established through this step which was executed three times.  

The essential connection between simulated devices and Azure IoT Hub occurs through connection strings. The unique identifiers consisting mainly of the primary connection string hold all essential authentication details and routing parameters. The simulated sensors employed the connection strings stored securely in the .env file of IoT simulation code to transmit data to their designated IoT Hub endpoints.  

## Setting Up Azure Stream Analytics Job  
The processing of live sensor data occurs within Azure Stream Analytics. To begin with our setup required the creation of a Stream Analytics job together with its connection to a designated Azure Blob Storage account to keep record of output data. The project team selected cost-saving measures through choosing one-third of the streaming unit size (1/3 SU).  

The Stream Analytics job required an output sink definition that led data to a specific container area inside the Azure Blob Storage account. The generic initial naming needs to be changed to 'IceConditionLogs' for better clarity regarding stored data purposes. The data output was set to JSON array format which made the data processing more efficient by allowing easy analysis and parsing of the processed information.  

## Querying Azure Stream Analytics  
Real-time data processing begins with the Stream Analytics query which functions as its base operation. The fundamental query illustrates continuous transportation of raw data from input into the specified output datastorageoutput through SELECT * INTO [datastorageoutput] FROM [input].  

The event-based stream query specified conditions for Unsafe ice detection while generating its dedicated data storage output. The implementation of aggregation queries enabled calculation of average ice thickness measurements within specific periods for providing decision-making insights.  

## Azure Blob Storage
The processed data ends up in Azure Blob Storage. I established the storage account through configuration of basic parameters with network permission activation and selection of locally redundant storage for durable data preservation.  

The storage container for processed sensor logs was set up in the storage account through default configurations.  

## Findings
The Stream Analytics job showed successful results from receiving and processing simulated sensor data based on data transmitted through Azure IoT Hub according to overview metrics.  

The raw sensor readings stored in Azure Blob Storage adopted JSON array format inside the .json file which resided in container. The data processing and storage system functions properly based on the successful implementation assessment.  

The assignment and verification completion marked the end of the process where all Azure resources received deletion because of cost-saving measures.  

## Conclusion
The project achieved a complete implementation of real-time skateway monitoring through simulated IoT sensors and essential Azure cloud services for the Rideau Canal. The Python script became more efficient during the initial setup of IoT device simulation after making some changes that made it challenging to implement. 
