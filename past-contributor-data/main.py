import csv

json_data = [
    [
        "zchenyu", {
            "earliestCommitDate": "2023-09-01T22:57:35.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/monitoring/commit/9f7912067286f52c897f9d2faa3e462075c531af",
            "earliestCommitRepo": "knative-extensions/monitoring"
        }
    ],
    [
        "abhijeetgauravm", {
            "earliestCommitDate": "2023-09-05T14:36:17.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/pkg/commit/66bf5af149996e05bba9ee787b38321a4abaec19",
            "earliestCommitRepo": "knative/pkg"
        }
    ],
    [
        "KaranJagtiani", {
            "earliestCommitDate": "2023-09-06T06:32:12.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/815fe70fa08a139960cf8501039903e7c0f9b3a0",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "arsenetar", {
            "earliestCommitDate": "2023-09-12T01:25:18.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/997d8ef27e0d86da05f46e5f51f9fb831b476de5",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "theomessin", {
            "earliestCommitDate": "2023-09-12T02:33:15.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/operator/commit/c42751f958891c9e75462b864b36042fb8c85867",
            "earliestCommitRepo": "knative/operator"
        }
    ],
    [
        "JinVei", {
            "earliestCommitDate": "2023-09-12T04:48:51.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/3010cb8e2a7c1f0048e201bdfeb98fa1528f1c44",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "RealArtemiy", {
            "earliestCommitDate": "2023-09-13T08:51:36.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/ecf5bfefb2320b92b4936045d8b5b74ed4fe05d0",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "CodesbyUnnati", {
            "earliestCommitDate": "2023-09-18T09:47:43.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/661e5724a0a959bce0ff08d3b2dcd062d649e52b",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "MeenuyD", {
            "earliestCommitDate": "2023-09-18T15:24:19.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/networking/commit/6feaf0cf4a0e9083c5daeb206c9dbe519413030f",
            "earliestCommitRepo": "knative/networking"
        }
    ],
    [
        "husnialhamdani", {
            "earliestCommitDate": "2023-09-20T02:32:11.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/8a71d34283aab77b5945f1d2e858b273e3cd50d3",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "seongpyoHong", {
            "earliestCommitDate": "2023-09-21T20:55:18.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/d02702e1a6b117988344797c59ebe2c94d50929a",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "dnwe", {
            "earliestCommitDate": "2023-09-22T08:54:24.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/5c4461d0a616401a983136602d09a95fbff4e514",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "Priyansurout", {
            "earliestCommitDate": "2023-09-25T15:29:52.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/3736ab56e7d0c21a5f07a9969b81fcf5ff3a7227",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "harshsingh-24", {
            "earliestCommitDate": "2023-09-28T18:17:38.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/6631be7573832e26828ce5dcb7fdf5ffa020a354",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "Micah-Gafford", {
            "earliestCommitDate": "2023-09-28T20:38:33.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/d79909862f7170bc12877ffcf6f978ddf40924bc",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "HrrrXppp", {
            "earliestCommitDate": "2023-10-04T09:20:05.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/1b7a1b0e4df3a38b0d649c0b126e63b85cd86763",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "SYK-08", {
            "earliestCommitDate": "2023-10-13T05:23:54.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/868e904c426a4ecab33316a438e4892e537fdb8d",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "akagami-harsh", {
            "earliestCommitDate": "2023-10-18T19:32:56.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/3ef831c9b7e4f620d3dd574ee9c559780bfdb322",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "ofey404", {
            "earliestCommitDate": "2023-10-19T13:31:39.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/729b03c1c83cc11eb03d19bd06676ee3ff4c7250",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "vinfinity7", {
            "earliestCommitDate": "2023-10-20T02:27:50.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/9bef31340724223621b0e785c9e8b50a3f7bd5f8",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "tatodorov", {
            "earliestCommitDate": "2023-10-23T02:47:47.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/3011f84008e53845ca72f3be811c6f5647ca6f5e",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "yechuan51", {
            "earliestCommitDate": "2023-10-23T04:04:05.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/monitoring/commit/9e7371dfcb7a1f0ac8b81622ce8147229e241332",
            "earliestCommitRepo": "knative-extensions/monitoring"
        }
    ],
    [
        "SiBell", {
            "earliestCommitDate": "2023-10-26T10:00:09.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/0684dbece5add2404b10a9a52b8502ae76e26159",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "prushh", {
            "earliestCommitDate": "2023-11-07T21:28:46.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/func/commit/7af58b5eb49e48bfabc95a2e1a4dfe8a4291175a",
            "earliestCommitRepo": "knative/func"
        }
    ],
    [
        "AlexMichaelJonesNC", {
            "earliestCommitDate": "2023-11-14T09:38:55.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/68ea6fae2fedb7a9d2af444b0cad65c28e866f27",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "luckymrwang", {
            "earliestCommitDate": "2023-11-14T10:17:50.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/936ecbdb547d896d1ef260c17edb4131cfd1d2ae",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "yuzp1996", {
            "earliestCommitDate": "2023-11-14T10:53:28.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/304f5c06b1fa885dfb608bd2aeb83165a8498665",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "prakrit55", {
            "earliestCommitDate": "2023-11-17T07:59:09.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/dc965225f63560e79d11d6729a2c720c254b0db7",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "rajibmitra", {
            "earliestCommitDate": "2023-11-17T20:04:09.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/b8da68a57082173d9b0c353bb959e400f05b10a2",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "md-saif-husain", {
            "earliestCommitDate": "2023-11-22T15:43:30.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/64b48479ac78fce6a399c65875821cb41ebc55ad",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "heysourin", {
            "earliestCommitDate": "2023-11-23T19:14:33.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/636dfad29920e5a6f92a1ed874fc782cbfe82b89",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "navinag1989", {
            "earliestCommitDate": "2023-11-28T07:14:52.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/8e998cf09026a0e7ca9122fef05d91ded440bab3",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "yanggangtony", {
            "earliestCommitDate": "2023-12-07T15:43:23.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/operator/commit/cfea599a9a028e20816bbbdbac1dd496be22f204",
            "earliestCommitRepo": "knative/operator"
        }
    ],
    [
        "cdalar", {
            "earliestCommitDate": "2023-12-07T19:32:26.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/930a91b33e5c22b62b7affb5d9cb2301a7f4e078",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "Skeen", {
            "earliestCommitDate": "2023-12-10T11:34:23.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-rabbitmq/commit/ee3c8600b47e51c52056353d895bc65246ade5e8",
            "earliestCommitRepo": "knative-extensions/eventing-rabbitmq"
        }
    ],
    [
        "zainabhusain227", {
            "earliestCommitDate": "2023-12-14T05:58:36.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/ux/commit/98f6cda9ed4507cd7c28f68dc0ab4833c17c08da",
            "earliestCommitRepo": "knative/ux"
        }
    ],
    [
        "tikr7", {
            "earliestCommitDate": "2023-12-19T21:18:09.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/3e08c959ddaff6fece3c80bb6c48cb17066b4756",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "sharmaansh21", {
            "earliestCommitDate": "2023-12-20T13:17:37.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/client/commit/70805a67db57e5902613562cb893d343d23e5c83",
            "earliestCommitRepo": "knative/client"
        }
    ],
    [
        "shikharish", {
            "earliestCommitDate": "2023-12-22T20:04:48.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/0ed108c468be215c796a1b9faff20ff12aca0d6c",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "SD-13", {
            "earliestCommitDate": "2024-01-02T20:23:51.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/6dadadcda29db9ecd6cab90820ddc05049fb5099",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "professorabhay", {
            "earliestCommitDate": "2024-01-04T13:44:24.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/777922060214df6ba80eb598cdd0c6abb811da91",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "pawarpranav83", {
            "earliestCommitDate": "2024-01-12T14:19:26.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/c7520cccd86eb21acea197a9d91b67a70fe8ce36",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "octonawish-akcodes", {
            "earliestCommitDate": "2024-01-15T08:54:19.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/42af160c3cfc244e26fa7bcd5db2c670ebdcf326",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "jacksgt", {
            "earliestCommitDate": "2024-01-15T20:06:01.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/1e2faa3b3745f9e3f5a4786ae16e755e9bf90e66",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "lou-lan", {
            "earliestCommitDate": "2024-01-15T21:10:40.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/752314ea57cbb37ea1d81606718c94e3d0a712c0",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "Zazzscoot", {
            "earliestCommitDate": "2024-01-18T15:54:14.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/fb9be2b67bf6c616792ead891916cbcae5c980c7",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "sadath-12", {
            "earliestCommitDate": "2024-01-22T16:41:09.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/44ff98b38212a812337725924a7fcd58be526a86",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "joshualyon", {
            "earliestCommitDate": "2024-01-25T04:53:22.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/kn-plugin-operator/commit/cdc6654961bd077d1506ccb77473f35ca44b9129",
            "earliestCommitRepo": "knative-extensions/kn-plugin-operator"
        }
    ],
    [
        "lysliu", {
            "earliestCommitDate": "2024-01-26T08:10:46.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/c14943c4c31f09371457ddf4fccddac97e00e578",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "prashantrewar", {
            "earliestCommitDate": "2024-01-30T15:30:47.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/release/commit/ca423a01335d4e82a4dc95edd62c8b2c2f750bc6",
            "earliestCommitRepo": "knative/release"
        }
    ],
    [
        "yijie-04", {
            "earliestCommitDate": "2024-01-30T15:38:35.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/ff52881fc57db975af4ceefe589f50dcd7a01e92",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "Indrranil", {
            "earliestCommitDate": "2024-01-31T07:21:43.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/community/commit/e5b53ab8e124bca286ca5499124e7b9fe4c1453f",
            "earliestCommitRepo": "knative/community"
        }
    ],
    [
        "converge", {
            "earliestCommitDate": "2024-02-02T10:22:37.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/6380b7b6b4967ad216ee30a71dc01a4a1815cce2",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "nrrso", {
            "earliestCommitDate": "2024-02-06T14:54:49.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/community/commit/cf25fc353b962dd5f9c1c8e0b4800eb92e56af0d",
            "earliestCommitRepo": "knative/community"
        }
    ],
    [
        "supu2", {
            "earliestCommitDate": "2024-02-07T20:38:32.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/operator/commit/0f1bee4a554ec67c49963967e11e1d820481a7b6",
            "earliestCommitRepo": "knative/operator"
        }
    ],
    [
        "gunishmatta", {
            "earliestCommitDate": "2024-02-09T10:04:51.000Z",
            "earliestCommitUrl":
            "https://github.com/knative-extensions/eventing-kafka-broker/commit/d6a383fff58047078c232f83bdcbe9e88d402891",
            "earliestCommitRepo": "knative-extensions/eventing-kafka-broker"
        }
    ],
    [
        "Muhammad-Raiyan", {
            "earliestCommitDate": "2024-02-13T00:35:51.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/212577294ecd8319b6cb6389cf9bc8de47b4af79",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "amarflybot", {
            "earliestCommitDate": "2024-02-14T17:31:04.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/serving/commit/62839144d0e96088cfe469ad0de8bd2b707afb13",
            "earliestCommitRepo": "knative/serving"
        }
    ],
    [
        "Sanket-0510", {
            "earliestCommitDate": "2024-02-16T21:10:19.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/func/commit/d2fb76c39d5db6301a04ad78108c61e7da949a4b",
            "earliestCommitRepo": "knative/func"
        }
    ],
    [
        "igorchyts", {
            "earliestCommitDate": "2024-02-19T13:26:12.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/docs/commit/4477889942daf822cef25014d043f5df3ae4aa85",
            "earliestCommitRepo": "knative/docs"
        }
    ],
    [
        "satyampsoni", {
            "earliestCommitDate": "2024-02-19T14:06:06.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/eventing/commit/bb2c03b9d8794fc84588cb02f9de140296e5582e",
            "earliestCommitRepo": "knative/eventing"
        }
    ],
    [
        "ckcd", {
            "earliestCommitDate": "2024-02-20T07:44:05.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/networking/commit/630e71a2dbc7e948b1a016ed5f7ea0951aa78ebb",
            "earliestCommitRepo": "knative/networking"
        }
    ],
    [
        "mmejia02", {
            "earliestCommitDate": "2024-02-27T17:18:45.000Z",
            "earliestCommitUrl":
            "https://github.com/knative/ux/commit/2860bed4e3f48b194b5d8df55c86338108e6a8c4",
            "earliestCommitRepo": "knative/ux"
        }
    ]
]

with open('commits.csv', 'w', newline='', encoding='utf-8') as csvfile:
  writer = csv.writer(csvfile)

  writer.writerow(
      ['GitHub Username', 'Earliest Commit Date', 'Commit URL', 'Repository'])

  # Iterate over JSON data and write rows
  for item in json_data:
    username = item[0]
    commit_info = item[1]
    commit_date = commit_info['earliestCommitDate'].split('T')[
        0]  
    commit_url = f'=HYPERLINK("{commit_info["earliestCommitUrl"]}", "View Commit")'  # Making commit URL clickable
    repository = commit_info['earliestCommitRepo']

    # Making GitHub username clickable
    github_username = f'=HYPERLINK("https://github.com/{username}", "{username}")'

    writer.writerow([github_username, commit_date, commit_url, repository])

print("CSV file created successfully.")
