## Project Title
- Scrapy-Redis-MySQL Pipeline

## Project Abstract
- 수천개의 instance를 한번에 MySQL에 연결하게 되면 Max Connection의 문제가 발생하여 Redis를 중간 단계의 Queue로 사용

## Requirement
- scrapy >= 2.0
- Redis >= 6.2
- redis == 본인의 Elasticsearch 버전

## 실행방법
- Git에서 코드를 clone.
- clone한 코드를 본인의 scrapy pipeline과 같은 디렉터리에 복사.
- pipeline에 RedisQueue import 후 spider를 실행하면 redis로 수집한 데이터를 push 함.
- 별도의 process로 MySQL_Handler 코드를 inport 하고 add_data에 redis에서 pop한 데이터를 tuple로 변환.
- 그 후 item_insert를 실행 하면 MYSQL에 수집한 데이터를 원하는 개수씩 한번에 bulk insert.
- MySQL_Handler의 schema는 본인의 코드에 맞게 변경을 하여야 함.

## Todo List
- schema를 json이나 xml, excel과 같은 형식으로 넣으면 자동으로 분석하여 data를 insert하도록 MySQL Handler 변경 필요.

## Credit
- [Redis Message Queue](https://m.blog.naver.com/wideeyed/221370229153) 코드를 참조하여 개발.
