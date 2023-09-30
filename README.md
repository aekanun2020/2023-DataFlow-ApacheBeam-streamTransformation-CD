# Apache Beam Data Streaming Project

This project is designed to create a data pipeline using Apache Beam, facilitating data transfer from PubSub to BigQuery on the Google Cloud Platform (GCP).

## Table of Contents

- [สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้](#สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้)
- [Installation](#Installation)
- [Linux](#Linux)


## สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้

ซอฟต์แวร์ทั้งหมดในโปรเจคนี้ ทำงานอยู่บน docker container ซึ่งต้องการ Docker program ที่สามารถทำงานได้บน pc หรือ mac (intel/m1/m2) หรือ vm ทั้ง on-premises และ on-cloud โดยจะต้องมีซอฟต์แวร์ต่างๆ ประกอบด้วย:

- Docker version 24.0.5 และ Docker Compose version v2.12.2 หรือ Docker Desktop for Mac/Windows
- Google Cloud SDK กรณีการ run งานตามโปรเจคนี้เกิดขึ้นนอก environment ของ Google Cloud
- Resource system ที่ต้องการ: CPU อย่างน้อย 2 vCPU และ RAM อย่างน้อย 4 GB

## Installation

1. **Docker and Docker-compose** - ท่านสามารถทำตามขั้นตอนในหน้า 12, 14-15: [Follow the instructions here](https://docs.google.com/presentation/d/1USvOvbXAohymqWaNbYMfD3e23Z35aJO-hQUaY7y_JBA/edit#slide=id.g198e6c17f8f_0_201).
   
2. **Google Cloud SDK** - [Follow the instructions here](https://cloud.google.com/sdk/docs/install).

## Linux

คำสั่งที่ใช้ แก้ไข file เมื่อแก้ไขเรียบร้อยแล้ว กด ctrl+x กรณีต้องการบันทึกให้กด y กรณีไม่ต้องการบันทึกให้กด n แล้วตามด้วย enter:

   ```sh
   nano "file"
  