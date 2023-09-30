# Apache Beam Data Streaming Project

This project is designed to create a data pipeline using Apache Beam, facilitating data transfer from PubSub to BigQuery on the Google Cloud Platform (GCP).

## Table of Contents

- [สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้](#สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้)
- [Setting Up Your Google Cloud Platform (GCP) Environment](#setting-up-your-google-cloud-platform-gcp-environment)
- [Installation](#installation)
- [Testing](#testing)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้

การทำงานตามโปรเจคนี้สามารถใช้เครื่องคอมพิวเตอร์ pc และ mac (intel/m1/m2) หรือ vm ทั้ง on-premises และ on-cloud ที่ต้องมีซอฟต์แวร์ต่างๆ ประกอบด้วย:

- Docker version 24.0.5 และ Docker Compose version v2.12.2 หรือ Docker Desktop for Mac/Windows
- Google Cloud SDK กรณีการ run งานตามโปรเจคนี้เกิดขึ้นนอก environment ของ Google Cloud

## Setting Up Your Google Cloud Platform (GCP) Environment

Before you start with the installation, make sure to set up your GCP environment:

1. **Create a GCP Project** - [Follow the instructions here](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
   
2. **Enable the necessary APIs** - Enable the Dataflow, BigQuery, and Pub/Sub APIs in your GCP project.

3. **Create a Service Account** - Create a GCP service account with the necessary permissions and download the JSON key file.

4. **Set up the Environment Variable** - Set up the GOOGLE_APPLICATION_CREDENTIALS environment variable to point to the service account key file:

   ```sh
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your-service-account-file.json"
   ```


## Installation