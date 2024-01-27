``` sql
select count(1) from 
taxi_data_sep where lpep_pickup_datetime >= '2019-09-18' and lpep_pickup_datetime <'2019-09-19' and lpep_dropoff_datetime < '2019-09-19';



select * from taxi_data_sep limit 1;


select * from( 
select date(lpep_pickup_datetime) as day, sum(trip_distance) as total_value
from taxi_data_sep
group by date(lpep_pickup_datetime))a order by a.total_value desc;



select lpep_pickup_datetime, "PULocationID" from taxi_data_sep limit 100;

select z."LocationID",z."Borough", a.total_value from( 
select "PULocationID", sum(total_amount) as total_value
from taxi_data_sep
where lpep_pickup_datetime between '2019-09-18' and '2019-09-19'
group by "PULocationID"
order by "PULocationID")a left join 
zone_lookup z on a."PULocationID" = z."LocationID"
order by a.total_value desc


select z."Borough", sum(total_amount)
from taxi_data_sep a left join 
zone_lookup z on a."PULocationID" = z."LocationID"
where a.lpep_pickup_datetime between '2019-09-18' and '2019-09-19'
group by z."Borough"


```

terraform apply return
```
google_storage_bucket.demo-bucket: Refreshing state... [id=de-course-411610-demo-bucket]

Terraform used the selected providers to generate the
following execution plan. Resource actions are indicated
with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "demo_dataset1"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + max_time_travel_hours      = (known after apply)
      + project                    = "de-course-411610"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.demo_dataset: Creating...
google_bigquery_dataset.demo_dataset: Creation complete after 1s [id=projects/de-course-411610/datasets/demo_dataset1]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```