# BatteryTrackerServer

## Features

BatteryTrackerServer is a service that reduces the possibility of overcharging your device by tracking its battery level
periodically.

The server relies on REST API to receive your device's information and battery level.

It also comes with a GUI interface that displays and monitors your device's battery *(default one minute)*. Once the
device's battery reaches a specific level *(default 80%)*, the server notifies you to unplug the charged device.

This repository contains the backend server of the BatteryTrackerServer.

**NOTE:** This service is designed for **personal use only**. The service contains little to no security features like
device authetication.

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

## Installation

Install the server with pip

```bash
  pip install -r requirements.txt
  cd my-project
```

## API Reference

#### Register Device

```http
  POST /device/register
```

| Parameter       | Type     | Description                                                                                            |
|:----------------|:---------|:-------------------------------------------------------------------------------------------------------|
| `device_id`     | `string` | **Required**. Unique id to identify your device                                                        |
| `device_name`   | `string` | **Required**. Name of your device                                                                      |
| `battery_level` | `string` | **Required** **Required**. Your device's current battery level. (Only supply the **numerical values**) |

#### Unregister Device

```http
  DELETE /device/unregister
```

| Parameter   | Type     | Description                                               |
|:------------|:---------|:----------------------------------------------------------|
| `device_id` | `string` | **Required**. Unique id to identify your device in memory |

#### Send Battery Level

```http
  PUT /battery_level/update
```

| Parameter               | Type     | Description                                                                               |
|:------------------------|:---------|:------------------------------------------------------------------------------------------|
| `device_id`             | `string` | **Required**. Unique id to identify your device                                           |
| `current_battery_level` | `string` | **Required**. Your device's current battery level. (Only supply the **numerical values**) |

### Response

The response from the server contains the following parameters to provide the client with more information about their
request:

| Parameter      | Type     | Description                           |
|:---------------|:---------|:--------------------------------------|
| `service_code` | `string` | The status of the requested operation |
| `message`      | `string` | Error messages if any                 |

Refer to [response.py]() in `api/utils` directory to view learn more about the service codes implemented.

## Contributing

Feel free to edit the plugin and submit a pull request or open an issue on github to leave a feedback

## License

[MIT](https://choosealicense.com/licenses/mit/)

## FAQ

#### Why does this project exist in the first place?

As I do not have enough wall outlets near my working area, I have to get up and walk into another room to plug my
smartphone into wall outlet charger whenever I want to charge my smartphone.

With the fear of overcharging my smartphone, I have to constantly get up and check my smartphone. This process is time
consuming and I tend to forget that my smartphone is charging in the other room.

This system allows me to monitor my smartphone's battery level while I am doing my work on my computer and notify me
when my smartphone is done charging.

  