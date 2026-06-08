# İnteraktif Laboratuvar - Terminal ve Komut Günlüğü (Execution Log)

Bu doküman, "Dual-Mode Interactive Web Security Laboratory" projesinin yapılandırılması, dağıtımı ve siber saldırı/savunma simülasyonları sırasında Kali Linux terminali üzerinde yürütülen tüm teknik adımların ve komutların kronolojik bir kaydıdır.

## 1. Ortam Hazırlığı ve Kurulum
Projenin temel bağımlılıklarının kurulması ve GitHub üzerinden sistemimize klonlanması işlemleri:

```bash
# Projenin klonlanması ve ana dizine geçiş
git clone [https://github.com/keyvanarasteh/ResearchLab.git](https://github.com/keyvanarasteh/ResearchLab.git)
cd ResearchLab

# Python sanal ortamının (Virtual Environment) oluşturulması
python3 -m venv venv

# Sanal ortamın aktifleştirilmesi
source venv/bin/activate

# Gerekli kütüphanelerin (FastAPI, Uvicorn, Redis, Pydantic) kurulması
pip install -r requirements.txt
