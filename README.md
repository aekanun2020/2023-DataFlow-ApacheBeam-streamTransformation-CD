# Terra-Docker-BeamFlow Project

This project revolves around developing a data pipeline leveraging Apache Beam to streamline the data flow from PubSub to BigQuery within the Google Cloud Platform (GCP). Within this endeavor, our Beam code incorporates data cleansing routines and employs a Continuous Delivery (CD) strategy, orchestrated using Terraform and containerized through Docker.

## Table of Contents

- [สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้](#สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้)
- [Installation](#Installation)
- [Video](#Video)


## สิ่งที่ต้องเตรียมมาเพื่อทำงานกับโปรเจคนี้

ซอฟต์แวร์ทั้งหมดในโปรเจคนี้ ทำงานอยู่บน docker container ซึ่งต้องการ Docker program ที่สามารถทำงานได้บน pc หรือ mac (intel/m1/m2) หรือ vm ทั้ง on-premises และ on-cloud โดยจะต้องมีซอฟต์แวร์ต่างๆ ประกอบด้วย:

- Docker version 24.0.5 และ Docker Compose version v2.12.2 หรือ Docker Desktop for Mac/Windows
- Google Cloud SDK กรณีการ run งานตามโปรเจคนี้เกิดขึ้นนอก environment ของ Google Cloud
- Resource system ที่ต้องการ: CPU อย่างน้อย 2 vCPU และ RAM อย่างน้อย 4 GB


## Installation

1. **Docker and Docker-compose** - ท่านสามารถทำตามขั้นตอนในหน้า 12, 14: [Follow the instructions here](https://docs.google.com/presentation/d/1USvOvbXAohymqWaNbYMfD3e23Z35aJO-hQUaY7y_JBA/edit#slide=id.g198e6c17f8f_0_201).
   
2. **Google Cloud SDK** - [Follow the instructions here](https://cloud.google.com/sdk/docs/install).


## Video

1. **Video 1** - [Link for Video](https://video.aekanun.com/D6lfK5J1).
   
2. **Video 2** - [Link for Video](https://video.aekanun.com/JCTmB6tG).

3. **Video 3** - [Link for Video](https://video.aekanun.com/sD7z0Klh).
   
4. **Video 4** - [Link for Video](https://video.aekanun.com/P2BxRLz7).

5. **Video 5** - [Link for Video](https://video.aekanun.com/h7rvSJYv).
   
6. **Video 6** - [Link for Video](https://video.aekanun.com/6cRtmq3W).

7. **Video 7** - [Link for Video](https://video.aekanun.com/3khyWtVc).
   
8. **Video 8** - [Link for Video](https://video.aekanun.com/rN6S9bnr).

9. **Video 9** - [Link for Video](https://video.aekanun.com/b3DQzNnl).
