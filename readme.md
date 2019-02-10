## OurWork

Progress
---
#### Beginner:

| implemented        | page             | dependencies |
| ------------------ | ---------------- | ------------ |
| :white_check_mark: | Enroll           | Api: `POST /member/ -> { mentors: [ mentor1, mentor2 ]}`; Model: `mentorModel.predict(job, location)` |
| :exlamation:       | Select mentor    | Frontend: carry selected mentor to next page |
| :exlamation:       | Complete course  | Api: `POST /member/` (update track_progress to: Project); Frontend: assume the same course that the mentor has will be taken; Model: `modelSkills.predict(member.skills)` |
| :exlamation:       | Get project      | Api: `GET /member/:id/ -> { ..., assigned_project: projectJSON }` |
| :exlamation:       | Become mentor    | Frontend: assume static page |


#### Mentor:
Evaluate job request


Recommendations
---

- :white_check_mark: Create data model
- :exclamation: Create mapping (string <-> features)

Data generation
---
- :white_check_mark: Mockaroo generate features
- :white_check_mark: Populate database with generated data (translated with mapping)

API
---

- :white_check_mark: Create basic endpoints (REST)
- Create custom endpoints that will use the recomendation engine
  to produce soreted
  - Mentor fits (matching Members with track_progress Entry <-> Mentor (job, location)
  - Contract fits (matching Member with track_progress Project <-> Contract using field (skill)


UI/UX
---

Local host setup
---

```
$ ./setup.sh
$ ./start.sh
$ # not ready - ./db.populate.sh
```
