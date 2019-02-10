## OurWork

Progress
---
#### Beginner:

| implemented        | page             | dependencies |
| ------------------ | ---------------- | ------------ |
| :white_check_mark: | Enroll           | Api: `POST /member/ -> { mentors: [ mentor1, mentor2 ]}`; Model: `mentorModel.predict(job, location)` |
| :exclamation:       | Select mentor    | Frontend: carry selected mentor to next page |
| :exclamation:       | Complete course  | Api: `POST /member/` (update track_progress to: Project); Frontend: assume the same course that the mentor has will be taken; Model: `modelSkills.predict(member.skills)` |
| :exclamation:       | Get project      | Api: `GET /member/:id/ -> { ..., assigned_project: projectJSON }` |
| :exclamation:       | Become mentor    | Frontend: assume static page |


Machine Learning
---

### Notes
* While debugging ok to use `.csv` data, but in "production" we will be training the model again every time (k-nearest is really fast, basically no training required, so we can afford it)

#### User facing api

```python
# ml.py -- models

class mentor
    # only mentor rows will be passe
    def train([ mentor_feature_row ])

    # only entry rows will be passed
    # returns -> sorted array of ids of closest mentors by (industry, location)
    def predict(industry_feature_int, location_feature_int)

class skill
    # args: contracts feature row array (skills one-hot encoding)
    def train([ contract_feature_row ])

    # args: single member's skills one-hot array
    # returns: best matching project id (k-nearest k = 1)
    def predict(project_ready_member_skills_features)
```

``` python
# ml.py -- to_features

def to_background_feature(industry_string, location_string) -> [ int, int ] ??
def to_skills_feature(array_string_skill_names) -> one hot array
```


#### Api interop
* Create two-way mappings `features <-> model fields`
  1. job `string <-> one hot` `ml.mentor`
  2. location `"int" <-> int` `ml.mentor`
  3. skills `"0,1,0,0" <-> List<bool>` `ml.job`

#### Data generation

- :white_check_mark: Mockaroo generate features
- :white_check_mark: Populate database with generated data (translated with mapping)

API
---

1. :white_check_mark: create member account **Enroll**
   `POST /member/ <- { id, job, location }`
2. :white_check_mark: get `[ mentor | track ]` recomendation `[ **Select mentor** | **Enroll in course** ]`
   * `GET /member/:id -> { ..., mentors: "id1,id2,id3", track: "my_mentor's track" }`
   * `[ GET /member/:id for id in string_to_array(mentors) ]`
3. :white_check_mark: **Complete course**
   `POST /member/ <- { ..., id: id, track_progress: "Project" }` (before save assign best matching project)
4. :white_check_mark: **Complete project**
   `POST /member/ <- { ..., id: id, track_progress: "Mentor" }` (now I can get recommended as a mentor)

Local host setup
---

```
$ ./setup.sh # install dependencies
$ ./start.sh # start server
$ ./populate.sh # somewhat ready, also need to call ./dropdb.sh whithin
```

#### After changing data model
```
$ ./sync.sh # create migrations, migrate
```
