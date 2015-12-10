#  Get current bills from Sunlight and add to database Bills table
  import sunlight
  import json
  from sunlight import openstates
  id_bill_json = openstates.bills(
    state = 'id',
    search_window = 'session')
  id_bills = byteify(json.dumps(id_bills_json))
  for bill in id_bills_json:
    bill_adder = Bill(bill["bill_id"], bill["session"], bill["title"], bill["id"], bill["updated_at"])
    db.session.add(bill_adder)
    db.session.commit()

# Strip html tags (from milkypostman on stackoverflow
from BeautifulSoup import BeautifulSoup

def removeTags(html, *tags):
    soup = BeautifulSoup(html)
    for tag in tags:
        for tag in soup.findAll(tag):
            tag.replaceWith("")

    return soup