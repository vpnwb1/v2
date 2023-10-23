package main

import (
"fmt"
"io/ioutil"
"log"
"net/http"
"regexp"
"strconv"
"strings"

"github.com/PuerkitoBio/goquery"
)

var client = &http.Client{}

func main() {

channels := []string{	
	"https://t.me/s/ip_cf",	
}

output := ""

myregex := map[string]string{
"ss":     `(.{3})ss:\/\/`,
"vmess":  `vmess:\/\/`,
"trojan": `trojan:\/\/`,
"vless":  `vless:\/\/`,
"ssr":    `ssr:\/\/`,
"hy2":    `hy2:\/\/`,
"tuic":   `tuic:\/\/`,
}

for i := 0; i < len(channels); i++ {
all_messages := false
if strings.Contains(channels[i], "{all_messages}") {
all_messages = true
channels[i] = strings.Split(channels[i], "{all_messages}")[0]
}

req, err := http.NewRequest("GET", channels[i], nil)
if err != nil {
log.Fatalf("Error When requesting to: %d Error : %s", channels[i], err)
}

resp, err1 := client.Do(req)
if err1 != nil {
log.Fatal(err1)
}
defer resp.Body.Close()

doc, err := goquery.NewDocumentFromReader(resp.Body)
if err != nil {
log.Fatal(err)
}

messages := 10
link, exist := doc.Find(".tgme_widget_message_wrap .js-widget_message").Last().Attr("data-post")
if messages < 100 && exist == true {
number := strings.Split(link, "/")[1]
fmt.Println(number)

doc = GetMessages(100, doc, number, channels[i])
}

if all_messages {
fmt.Println(doc.Find(".js-widget_message_wrap").Length())
doc.Find(".tgme_widget_message_text").Each(func(j int, s *goquery.Selection) {
message_text := s.Text()
lines := strings.Split(message_text, "\n")
for a := 0; a < len(lines); a++ {
for _, regex_value := range myregex {
re := regexp.MustCompile(regex_value)
lines[a] = re.ReplaceAllStringFunc(lines[a], func(match string) string {
return "\n" + match
})
}
output += lines[a] + "\n"
}
})
} else {
doc.Find("code,pre").Each(func(j int, s *goquery.Selection) {
message_text := s.Text()
lines := strings.Split(message_text, "\n")
for a := 0; a < len(lines); a++ {
for proto_regex, regex_value := range myregex {
re := regexp.MustCompile(regex_value)
lines[a] = re.ReplaceAllStringFunc(lines[a], func(match string) string {
if proto_regex == "ss" {
if match[:3] == "vme" {
return "\n" + match
} else if match[:3] == "vle" {
return "\n" + match
} else if match[:3] == "ssr" {
return "\n" + match
} else {
return "\n" + match
}
} else {
return "\n" + match
}
})

if len(strings.Split(lines[a], "\n")) > 1 {
myconfigs := strings.Split(lines[a], "\n")
for i := 0; i < len(myconfigs); i++ {
if myconfigs[i] != "" {
re := regexp.MustCompile(regex_value)
myconfigs[i] = strings.ReplaceAll(myconfigs[i], " ", "")
match := re.FindStringSubmatch(myconfigs[i])
if len(match) >= 1 {
if proto_regex == "ss" {
if match[1][:3] == "vme" {
output += myconfigs[i] + "\n"
} else if match[1][:3] == "vle" {
output += myconfigs[i] + "\n"
} else if match[1][:3] == "ssr" {
output += myconfigs[i] + "\n"
} else {
output += myconfigs[i][3:] + "\n"
}
} else {
output += myconfigs[i] + "\n"
}
}
}
}
}
}
}
})
}
}

WriteToFile(output, "ready/fromtele.txt")
}

func WriteToFile(fileContent string, filePath string) {
err := ioutil.WriteFile(filePath, []byte(fileContent), 0644)
if err != nil {
fmt.Println("Error writing file:", err)
return
}

fmt.Println("File written successfully")
}

func load_more(link string) *goquery.Document {
req, _ := http.NewRequest("GET", link, nil)
fmt.Println(link)
resp, _ := client.Do(req)
doc, _ := goquery.NewDocumentFromReader(resp.Body)
return doc
}

func GetMessages(length int, doc *goquery.Document, number string, channel string) *goquery.Document {
x := load_more(channel + "?before=" + number)

html2, _ := x.Html()
reader2 := strings.NewReader(html2)
doc2, _ := goquery.NewDocumentFromReader(reader2)

// _, exist := doc.Find(".js-messages_more").Attr("href")
doc.Find("body").AppendSelection(doc2.Find("body").Children())

newDoc := goquery.NewDocumentFromNode(doc.Selection.Nodes[0])
// fmt.Println(newDoc.Find(".js-messages_more").Attr("href"))
messages := newDoc.Find(".js-widget_message_wrap").Length()

fmt.Println(messages)
if messages > length {
return newDoc
} else {
num, _ := strconv.Atoi(number)
n := num - 21
if n > 0 {
ns := strconv.Itoa(n)
GetMessages(length, newDoc, ns, channel)
} else {
return newDoc
}
}

return newDoc
}

func reverse(lines []string) []string {
for i := 0; i < len(lines)/2; i++ {
j := len(lines) - i - 1
lines[i], lines[j] = lines[j], lines[i]
}
return lines
}

func RemoveDuplicate(config string) string {
lines := strings.Split(config, "\n")

// Use a map to keep track of unique lines
uniqueLines := make(map[string]bool)

// Loop over lines and add unique lines to map
for _, line := range lines {
if len(line) > 0 {
uniqueLines[line] = true
}
}

// Join unique lines into a string
uniqueString := strings.Join(getKeys(uniqueLines), "\n")

return uniqueString
}

func getKeys(m map[string]bool) []string {
keys := make([]string, len(m))
i := 0
for k := range m {
keys[i] = k
i++
}
return keys
}