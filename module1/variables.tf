variable "credentials" {
  description = "My Credentials"
  default     = "../keys/creds.json"
}

variable "project" {
  description = "Project"
  default     = "de-course-411610"
}

variable "region" {
  description = "Region"
  #Update the below to your desired region
  default = "us-central1"
}

variable "bq_dataset_name" {
  description = "My Bigquery Dataset Name"
  default     = "demo_dataset1"
}

variable "gcs_storage_class" {
  description = "Bucket Storage class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "My storage Bucket Name"
  default     = "de-course-411610-demo-bucket"

}

variable "location" {
  default     = "US"
  description = "Project Location"

}
