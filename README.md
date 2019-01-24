# Detect sentiment from customer reviews using Amazon Comprehend

<p> In today’s world, public content has never been more relevant. Data from customer reviews is being used as a tool to gain insight into consumption-related decisions as the understanding of its associated sentiment grants businesses invaluable market awareness and the ability to proactively address issues early.

Sentiment analysis uses a process to computationally determine whether a piece of writing is positive, negative, neutral, or mixed. Amazon Comprehend is a natural language processing (NLP) text analytics service made up of a handful of APIs that allows you to detect sentiment (along with key phrases, named entities, and language) and perform topic modeling from a collection of documents. The service’s ability to detect sentiment is done using state-of-the-art deep learning algorithms that use scoring mechanisms and attributes during the evaluation of text. The Amazon Comprehend training data set primarily consists of data found in product descriptions and consumer reviews from one of the largest natural language collections in the world — Amazon.com. We give you a fully trained model that continuously retrains against new data to keep pace with the evolution of language. ML in general requires a different skillset than most data engineers and developers currently have. Amazon Comprehend has removed this gap and made NLP easy to consume using the skills developers already have.

In this blog post, we will show you how to leverage Amazon Comprehend as part of a serverless event driven architecture, built with AWS services, to detect customer sentiment. </p>

<p><em> Solution Architecture Overview </em></p>
<img src="BlogFoto/ComprehendReviewSentimentArchitecture.png" alt="Architecture" title="Amazon Comprehend Review Sentiment Architecture" align="center" />

